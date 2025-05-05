#!/bin/bash

#WINDOWS
WSL_HOME_DIR=~/workspace
WINDOWS_APP_FOLDER=/mnt/c/Workspace/My-Applications/GitHub/repository
WINDOWS_VIDEO_FOLDER=/mnt/c/Users/ikitsakis/Videos/ToTranscribe

#UBUNTU
# WSL_HOME_DIR=~/Workspace/repository
# WINDOWS_VIDEO_FOLDER=~/Videos/ToTranscribe

WHISPER_DIR=$WSL_HOME_DIR/transcriber-app/whisper.cpp
BUILD_DIR=$WHISPER_DIR/build/bin


# cp -r $WINDOWS_APP_FOLDER/transcriber-app $WSL_HOME_DIR/
cp $WINDOWS_VIDEO_FOLDER/*.mp4 $WSL_HOME_DIR/transcriber-app/input/

cd $WSL_HOME_DIR/transcriber-app
git clone https://github.com/ggerganov/whisper.cpp
cd whisper.cpp
make
cd ..


echo "🎯 Select Whisper model to download:"
echo "1 → small (Multilingual, English+Greek)"
echo "2 → medium (Multilingual, English+Greek)"
echo "3 → large-v2 (Best multilingual, biggest size)"
read -p "Select [1-3]: " model_choice

case $model_choice in
    1)
        MODEL_NAME="small"
        ;;
    2)
        MODEL_NAME="medium"
        ;;
    3)
        MODEL_NAME="large-v2"
        ;;
    *)
        echo "❗ Invalid choice. Defaulting to medium.en."
        MODEL_NAME="medium.en"
        ;;
esac
echo "📦 Downloading model: $MODEL_NAME ..."
# Step 1: Ensure download script is executable
chmod +x $WHISPER_DIR/models/download-ggml-model.sh

# Step 2: Download model
$WHISPER_DIR/models/download-ggml-model.sh $MODEL_NAME

# Step 3: Check and build quantize if needed
if [ ! -f "$BUILD_DIR/quantize" ]; then
    echo "🔧 quantize not found, building it..."
    cd $WHISPER_DIR
    make
    cd -
fi

# Step 4: Quantize model
$BUILD_DIR/quantize \
    $WHISPER_DIR/models/ggml-$MODEL_NAME.bin \
    models/ggml-$MODEL_NAME-q5_0.bin q5_0

echo "✅ Done downloading and quantizing $MODEL_NAME model!"
