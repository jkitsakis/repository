import openai
import vosk
import datetime
import json
import os
import config
import re

# 🧠 Greek phonetic corrections for technical terms
PHONETIC_GREEK_CORRECTIONS = {
    "f1 σκορ": "f1 score",
    "άνταμ όπτιμαϊζερ": "adam optimizer",
    "άντερφιτινγκ": "underfitting",
    "άντι μονότονικ πρόπερτι": "anti-monotonic property",
    "άουτλάιερ ντετέξιον": "outlier detection",
    "άπριορι": "apriori",
    "έντροπι": "entropy",
    "αγκλομερατιβ": "agglomerative",
    "ακκιούραση": "accuracy",
    "ακτιβέισιον φάνκσιον": "activation function",
    "αντζάστεντ αρ σκουέρντ": "adjusted r-squared",
    "αουκ": "auc",
    "αρ": "r",
    "αρ εν εν": "rnn",
    "αρ μάρκνταουν": "rmarkdown",
    "αρ σκουέρντ": "r-squared",
    "αρία αντερ δε κερβ": "area under the curve",
    "αρίμα": "arima",
    "ασοσιέισιον ρουλ": "association rule",
    "βάλιντέισιον": "validation set",
    "βέριανς": "variance",
    "γκάουσιαν μίξτουρ μόδελ": "gaussian mixture model",
    "γκρεντιεντ ντισσέντ": "gradient descent",
    "γκριντ σερτς": "grid search",
    "γουέρκφλοου": "workflow",
    "γουόρντ του βεκ": "word2vec",
    "εκπαίδευση": "training",
    "ελ ες τι έμ": "lstm",
    "ελ ντι έι": "lda",
    "ελ ουάν": "l1",
    "ελ του": "l2",
    "εμ έλ": "ML",
    "εμ ες ι": "mse",
    "εν έλ πι": "nlp",
    "ενσαμπλ": "ensemble",
    "εξ τζι μπούστ": "xgboost",
    "εποχή": "epoch",
    "ερρρ φάνκσιον": "error function",
    "εφ ένα σκορ": "f1-score",
    "εϊ αϊ": "AI",
    "ζή σκορ": "z-score",
    "ζή σκορ νορμαλαϊζέισιον": "z-score normalization",
    "ι εν χίλια εβδομήντα ένα": "e1071",
    "ιμπιουτέισιον": "imputation",
    "ινφορμέισιον γκέιν": "information gain",
    "κάι σκουέρ τεστ": "chi-square test",
    "κάρετ": "caret",
    "κέρας": "keras",
    "κέρς οφ νταϊμενσιονάλιτι": "curse of dimensionality",
    "καν": "knn",
    "κέι εν εν": "knn",
    "κατ μπούστ": "catboost",
    "κερτόσις": "kurtosis",
    "κεϊ μηνς": "k-means",
    "κλάσιφικέισιον": "classification",
    "κλάστερινγκ": "clustering",
    "κοντίσιοναλ προμπαμπίλιτι": "conditional probability",
    "κονφάουντινγκ βαριαμπλ": "confounding variable",
    "κονφιουζον μάτριξ": "confusion matrix",
    "κρος έντροπι": "cross-entropy",
    "κρος βαλιντέισιον": "cross-validation",
    "κόνφιντενς": "confidence",
    "κόνφιντενς ίντερβαλ": "confidence interval",
    "λάικλιχουντ": "likelihood",
    "λάιτ τζι μπι έμ": "lightgbm",
    "λάσσο": "lasso",
    "λέιμπελ ενκόντινγκ": "label encoding",
    "λέρνινγκ ρέιτ": "learning rate",
    "λαγκ": "lag",
    "λεμματιζέισιον": "lemmatization",
    "λινεαρ ρεγκρέσιον": "linear regression",
    "λιφτ": "lift",
    "λογ λος": "log loss",
    "λοτζίστικ ρεγκρέσιον": "logistic regression",
    "λόσ φάνκσιον": "loss function",
    "μάξιμουμ λάικλιχουντ εστιμέισιον": "maximum likelihood estimation",
    "μάτριξ": "matrix",
    "μήντιαν": "median",
    "μίσσινγκ βάλιουζ": "missing values",
    "μασίν λέρνινγκ": "machine learning",
    "ματπλότλιμπ": "matplotlib",
    "μιμ μαξ σκέιλινγκ": "min-max scaling",
    "μιν": "mean",
    "μιν άμπσολουτ έρορ": "mean absolute error",
    "μιν σιφτ": "mean shift",
    "μιν σκουέρντ έρορ": "mean squared error",
    "μπάγκινγκ": "bagging",
    "μπάιας": "bias",
    "μπέιζ θίορεμ": "bayes theorem",
    "μπέιζιαν ίνφερενς": "bayesian inference",
    "μπακπροπαγκέισιον": "backpropagation",
    "μπερτ": "bert",
    "μπιγκ ντέιτα": "big data",
    "μπούστινγκ": "boosting",
    "μόντελ ντιπλόιμεντ": "model deployment",
    "μόουντ": "mode",
    "ναλ χαϊπόθεσις": "null hypothesis",
    "ναϊβ μπέις": "naive bayes",
    "νειμπορς":"neighbours",
    "νευρωνικά δίκτυα": "neural networks",
    "νιούραλ νέτγουερκ": "neural network",
    "νορμαλαϊζέισιον": "normalization",
    "νούμπαϊ": "numpy",
    "ντέιτα βιζουαλαιζέισιον": "data visualization",
    "ντέιτα κλίνινγκ": "data cleaning",
    "ντέιτα πάιπλάιν": "data pipeline",
    "ντέιτα ράνγκλινγκ": "data wrangling",
    "ντέιτα σάιενς": "data science",
    "ντένδρογκραμ": "dendrogram",
    "ντι έλ": "DL",
    "ντι μπι σκαν": "DBSCAN",
    "ντι πι ελ γουάαρ": "dplyr",
    "ντιπ λέρνινγκ": "deep learning",
    "ντισιζιον τρι": "decision tree",
    "ντρόπαουτ": "dropout",
    "οτοκορελέισιον": "autocorrelation",
    "ουαν χοτ ενκόντινγκ": "one-hot encoding",
    "πάιπλάιν": "pipeline",
    "πάιτορτς": "pytorch",
    "πάντας": "pandas",
    "πι βάλλιου": "p-value",
    "πι σι ε": "pca",
    "ποστέριαρ": "posterior",
    "πράιορ": "prior",
    "πρίνσιπαλ κομπόουνεντ αναλύσις": "principal component analysis",
    "πρεσίζιον": "precision",
    "προμπαμπίλιτυ": "probability",
    "ράντομ σερτς": "random search",
    "ρέγκιουλαριζέισιον": "regularization",
    "ρέλου": "relu",
    "ρεγκρέσιον": "regression",
    "ρικόλ": "recall",
    "ριτζ": "ridge",
    "ροκ κερβ": "roc curve",
    "ρόλλινγκ άβεριτζ": "rolling average",
    "σάικιτ λερν": "scikit-learn",
    "σάμπλινγκ ντιστριμπιούσιον": "sampling distribution",
    "σέντραλ λίμιτ θίορεμ": "central limit theorem",
    "σίγκμοιντ": "sigmoid",
    "σίμπορν": "seaborn",
    "σβμ": "support vector machine",
    "σενσιτίβιτι": "sensitivity",
    "σι εν εν": "cnn",
    "σιζονάλιτι": "seasonality",
    "σιλουέτ σκορ": "silhouette score",
    "σκιούνεσς": "skewness",
    "σουπόρτ": "support",
    "σοφτ κλάστερινγκ": "soft clustering",
    "σοφτμαξ": "softmax",
    "σπεσιφίσιτι": "specificity",
    "στακινγκ":"stacking",
    "στάτς μόουντελς": "statsmodels",
    "στέμινγκ": "stemming",
    "στένταρντ ντεβιαίισιον": "standard deviation",
    "στέσιοναριτι": "stationarity",
    "στανταρνταϊζέισιον": "standardization",
    "τένσορφλοου": "tensorflow",
    "τανχ": "tanh",
    "τεξτ κλάσιφικέισιον": "text classification",
    "τεστ σετ": "test set",
    "τζι τζι πλοτ 2": "ggplot2",
    "τι ες εν ι": "tsne",
    "τι εφ άι ντι εφ": "tf-idf",
    "τι τεστ": "t-test",
    "τοκενιζέισιον": "tokenization",
    "τρέιν τεστ σπλιτ": "train-test split",
    "τρέινινγκ σετ": "training set",
    "τρανσφόρμερ": "transformer",
    "τρεντ": "trend",
    "τυχαίο δάσος": "random forest",
    "φίτσουρ εξτράξιον": "feature extraction",
    "φίτσουρ ιμπόρτανς": "feature importance",
    "φίτσουρ σελέξιον": "feature selection",
    "φίτσουρ σκέιλινγκ": "feature scaling",
    "φρίκουεντ άιτεμσετ": "frequent itemset",
    "χάιπερ παραμίτερ τούνινγκ": "hyperparameter tuning",
    "χαρντ κλάστερινγκ": "hard clustering",
    "χαϊεράρικαλ κλάστερινγκ": "hierarchical clustering",
    "χαϊπόθεσις τέστινγκ": "hypothesis testing",
    "όβερφιτινγκ": "overfitting",
}

def correct_technical_terms(text):
    print(f"Refined text 1 : {text}")
    for greek, english in PHONETIC_GREEK_CORRECTIONS.items():
        text = text.replace(greek, english)
    print(f"Refined text 2 : {text}")
    return text


class AssistantEngine:
    def __init__(self):
        openai.api_key = config.OPENAI_API_KEY
        self.models = {}
        self.language_choice = config.DEFAULT_LANGUAGE
        self.question_counter = 0
        self.load_all_vosk_models()

    def load_all_vosk_models(self):
        for lang in config.AVAILABLE_LANGUAGES:
            model_subpath = config.LANGUAGE_MODEL_MAP.get(lang)
            model_path = os.path.join(config.MODEL_FOLDER, model_subpath)
            if not os.path.exists(model_path):
                print(f"⚠️ Model for {lang} not found at {model_path}")
                continue
            self.models[lang] = vosk.Model(model_path)
            print(f"✅ Loaded Vosk model for {lang}")

    def recognize_audio(self, recorded_audio):
        model = self.models.get(self.language_choice)
        if not model:
            raise Exception(f"No model loaded for language {self.language_choice}")
        recognizer = vosk.KaldiRecognizer(model, 16000)
        recognizer.AcceptWaveform(recorded_audio)
        result = recognizer.Result()
        text = json.loads(result).get("text", "")
        return correct_technical_terms(text.strip())

    def refine_question(self, raw_text):
        try:
            protected_map = {}
            masked_text = raw_text
            # for i, term in enumerate(config.PROTECTED_TERMS):
            #     pattern = re.compile(re.escape(term), re.IGNORECASE)
            #     if pattern.search(masked_text):
            #         key = f"<TERM{i}>"
            #         protected_map[key] = term
            #         masked_text = pattern.sub(key, masked_text)

            refine_prompt = (
                f"You are {config.ROLE} in oral examination. Give a short answer in Greek"
            )


            client = openai.OpenAI(api_key=config.OPENAI_API_KEY)
            response = client.chat.completions.create(
                model=config.OPENAI_MODEL,
                messages=[
                    {"role": "system", "content": refine_prompt},
                    {"role": "user", "content": masked_text}
                ]
            )
            refined = response.choices[0].message.content.strip()

            for key, term in protected_map.items():
                refined = refined.replace(key, term)
            return refined
        except Exception as e:
            print(f"Error refining question: {e}")
            return raw_text

    def ask_ai(self, question):
        try:
            system_prompt = (f"You are a {config.ROLE}. Please type a suitable answer for oral examination . "
                             f"If possible in bullets to easy reading. "
                             f"Give a short Answer in simple greek ")
            client = openai.OpenAI(api_key=config.OPENAI_API_KEY)
            response = client.chat.completions.create(
                model=config.OPENAI_MODEL,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": question}
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error asking AI: {e}"

    def log_session(self, question, answer):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(config.SESSION_LOG_FILE, "a", encoding="utf-8") as f:
            f.write(f"\n[{timestamp}]\nQ: {question}\nA: {answer}\n" + "-"*50 + "\n")

    def next_question_number(self):
        self.question_counter += 1
        return self.question_counter
