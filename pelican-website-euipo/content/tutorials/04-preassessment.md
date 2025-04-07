Title: Pre-Assessment
Slug: preAssessment
Summary: Pre-Assessment Backend
order: 04

# Pre-Assessment Backend – Controller Documentation

This document provides a domain-level overview and functional description of all REST controllers in the **pre-assessment-backend** project.

---

## 📁 Domain: Form Management

Handles the lifecycle of pre-assessment forms and user session-related endpoints.

### `FormController`
- Create, read, update, and delete assessment forms.
- Import data from trademarks.
- Export goods & services and generate warning reports.

### `RepresentationFormController`
- Submit different types of trademark representations (e.g., word, image, shape).
- Validate and preview representations.

### `DocumentsController`
- Upload and download documents, especially for mark representation or evidence.

### `MeController`
- Returns the authenticated user's profile and session info.

### `UserController`
- Provides access to the user’s draft forms with pagination support.

### `LogoutController`
- Terminates user session securely.

---

## 🔐 Domain: Validation & Legal Checks

Performs evaluations of the form against legal and registry rules.

### `DeceptivenessController`
- Analyzes if the proposed mark may mislead consumers.

### `OffensivenessController`
- Checks if a trademark is offensive culturally, politically, or socially.

### `NonDistinctivenessController`
- Determines if a trademark lacks inherent distinctiveness.

### `FlagsAndSymbolsController`
- Detects illegal use of protected national or institutional symbols.

### `GeographicalIndicationsController`
- Flags conflict with protected Geographical Indications (e.g., “Champagne”).

### `TraditionalSpecialitiesController`
- Validates names against Traditional Speciality Guaranteed (TSG) foods.

### `TraditionalWinesController`
- Checks trademark for violations of traditional wine terms (TTW).

---

## 🧠 Domain: Trademark Intelligence

Connects with external trademark databases to assess similarity or reuse data.

### `SearchTrademarkController`
- Search trademarks, fetch metadata and preview associated imagery.

### `EarlierTrademarksController`
- Finds potential conflicts with earlier trademarks.
- Exportable as Excel/CSV reports.

### `SimilarDecisionsController`
- Shows past legal decisions that resemble current submission.
- Supports exporting detailed legal precedents.

---

## 📦 Domain: Goods & Services Management

Provides tooling for managing Nice Classification terms and validations.

### `GoodsAndServicesController`
- Bulk import goods/services lists.
- Fetch prefix categories.

### `GoodsAndServicesComparisonController`
- Compares current G&S with those of existing trademarks.
- Generates PDF comparison reports.

### `TermsController`
- Lookup individual classification terms.

### `TaxonomyController`
- Retrieve classification taxonomy structure based on language.

### `SuggestionController`
- Returns AI/logic-based suggestions for terms.

### `ClassificationValidationController`
- Verifies if classification terms are valid for the jurisdiction.

### `ClassificationTranslationController`
- Translates goods/services terms between languages.

### `ClassesController`
- Returns the full list of Nice classification classes.

---

## ⚙️ Domain: Configuration & Reporting

Supports frontend configuration and tool setup.

### `ConfigurationController`
- Provides global configuration flags, analytics (Matomo), and Sentry setup.
- Supplies i18n literals.

### `PreAssessmentController`
- Returns feature availability and preassessment tool configuration per mode (e.g., basic, advanced).

---


<h2>Use Case Overview</h2>
<div class="scroll-wrapper">
<table border="1" class="dataframe scroll-table">
  <thead>
    <tr style="text-align: right;">
      <th>UseCase</th>
      <th>ImplementsPort</th>
      <th>RelatedServices</th>
      <th>WebClientUsedInImpl</th>
      <th>ServiceImplClasses</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>AddDocument.java</td>
      <td>AddDocumentPort</td>
      <td>documentRepositoryService</td>
      <td>DocumentRepositoryServiceImpl: 1 WebClient file(s)</td>
      <td>DocumentRepositoryServiceImpl</td>
    </tr>
    <tr>
      <td>CheckCpvo.java</td>
      <td>CheckCpvoPort</td>
      <td>agSupportService</td>
      <td>AgSupportServiceImpl: 1 WebClient file(s)</td>
      <td>AgSupportServiceImpl</td>
    </tr>
    <tr>
      <td>CheckDeceptiveness.java</td>
      <td>CheckDeceptivenessPort</td>
      <td>agSupportService</td>
      <td>AgSupportServiceImpl: 1 WebClient file(s)</td>
      <td>AgSupportServiceImpl</td>
    </tr>
    <tr>
      <td>CheckEarlierTrademarks.java</td>
      <td>CheckEarlierTrademarksPort</td>
      <td>proceedingIndicationsService, preAssessmentService, formApplicationService, trademarkSearchService</td>
      <td>ProceedingIndicationsServiceImpl: 1 WebClient file(s); PreAssessmentServiceImpl: 1 WebClient file(s); FormApplicationServiceImpl: 1 WebClient file(s); TrademarkSearchServiceImpl: 2 WebClient file(s)</td>
      <td>ProceedingIndicationsServiceImpl, PreAssessmentServiceImpl, FormApplicationServiceImpl, TrademarkSearchServiceImpl</td>
    </tr>
    <tr>
      <td>CheckFlagsAndSymbols.java</td>
      <td>CheckFlagsAndSymbolsPort</td>
      <td>preAssessmentService, formApplicationService</td>
      <td>PreAssessmentServiceImpl: 1 WebClient file(s); FormApplicationServiceImpl: 1 WebClient file(s)</td>
      <td>PreAssessmentServiceImpl, FormApplicationServiceImpl</td>
    </tr>
    <tr>
      <td>CheckGeographicalIndications.java</td>
      <td>CheckGeographicalIndicationsPort</td>
      <td>agSupportService</td>
      <td>AgSupportServiceImpl: 1 WebClient file(s)</td>
      <td>AgSupportServiceImpl</td>
    </tr>
    <tr>
      <td>CheckNonDistinctiveness.java</td>
      <td>CheckNonDistinctivenessPort</td>
      <td>preAssessmentService</td>
      <td>PreAssessmentServiceImpl: 1 WebClient file(s)</td>
      <td>PreAssessmentServiceImpl</td>
    </tr>
    <tr>
      <td>CheckOffensiveness.java</td>
      <td>CheckOffensivenessPort</td>
      <td>agSupportService</td>
      <td>AgSupportServiceImpl: 1 WebClient file(s)</td>
      <td>AgSupportServiceImpl</td>
    </tr>
    <tr>
      <td>CheckSimilarDecisions.java</td>
      <td>CheckSimilarDecisionsPort</td>
      <td>preAssessmentService</td>
      <td>PreAssessmentServiceImpl: 1 WebClient file(s)</td>
      <td>PreAssessmentServiceImpl</td>
    </tr>
    <tr>
      <td>CheckTraditionalSpecialitiesGuaranteed.java</td>
      <td>CheckTraditionalSpecialitiesGuaranteedPort</td>
      <td>agSupportService</td>
      <td>AgSupportServiceImpl: 1 WebClient file(s)</td>
      <td>AgSupportServiceImpl</td>
    </tr>
    <tr>
      <td>CheckTraditionalTermsForWines.java</td>
      <td>CheckTraditionalTermsForWinesPort</td>
      <td>agSupportService</td>
      <td>AgSupportServiceImpl: 1 WebClient file(s)</td>
      <td>AgSupportServiceImpl</td>
    </tr>
    <tr>
      <td>CreateForm.java</td>
      <td>CreateFormPort</td>
      <td>formApplicationService</td>
      <td>FormApplicationServiceImpl: 1 WebClient file(s)</td>
      <td>FormApplicationServiceImpl</td>
    </tr>
    <tr>
      <td>DeleteForm.java</td>
      <td>DeleteFormPort</td>
      <td>formApplicationService</td>
      <td>FormApplicationServiceImpl: 1 WebClient file(s)</td>
      <td>FormApplicationServiceImpl</td>
    </tr>
    <tr>
      <td>DownloadList.java</td>
      <td>DownloadListPort</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>DownloadWarningReport.java</td>
      <td>DownloadWarningReportPort</td>
      <td>formApplicationService, domainsExportService, validateTermsService, preAssessmentExportService, documentGeneratorService, agSupportExportService, trademarkSearchService</td>
      <td>FormApplicationServiceImpl: 1 WebClient file(s); DomainsExportServiceImpl: 1 WebClient file(s); PreAssessmentExportServiceImpl: 1 WebClient file(s); DocumentGeneratorServiceImpl: 1 WebClient file(s); AgSupportExportServiceImpl: 1 WebClient file(s); TrademarkSearchServiceImpl: 2 WebClient file(s)</td>
      <td>FormApplicationServiceImpl, DomainsExportServiceImpl, PreAssessmentExportServiceImpl, DocumentGeneratorServiceImpl, AgSupportExportServiceImpl, TrademarkSearchServiceImpl</td>
    </tr>
    <tr>
      <td>GetDocument.java</td>
      <td>GetDocumentPort</td>
      <td>documentRepositoryService</td>
      <td>DocumentRepositoryServiceImpl: 1 WebClient file(s)</td>
      <td>DocumentRepositoryServiceImpl</td>
    </tr>
    <tr>
      <td>GetDocumentContent.java</td>
      <td>GetDocumentContentPort</td>
      <td>documentRepositoryService</td>
      <td>DocumentRepositoryServiceImpl: 1 WebClient file(s)</td>
      <td>DocumentRepositoryServiceImpl</td>
    </tr>
    <tr>
      <td>GetForm.java</td>
      <td>GetFormPort</td>
      <td>formApplicationService</td>
      <td>FormApplicationServiceImpl: 1 WebClient file(s)</td>
      <td>FormApplicationServiceImpl</td>
    </tr>
    <tr>
      <td>GetFormDocument.java</td>
      <td>GetFormDocumentPort</td>
      <td>formApplicationService</td>
      <td>FormApplicationServiceImpl: 1 WebClient file(s)</td>
      <td>FormApplicationServiceImpl</td>
    </tr>
    <tr>
      <td>GetFormRepresentationDocument.java</td>
      <td>GetFormRepresentationDocumentPort</td>
      <td>formApplicationService</td>
      <td>FormApplicationServiceImpl: 1 WebClient file(s)</td>
      <td>FormApplicationServiceImpl</td>
    </tr>
    <tr>
      <td>GetGeographicalIndicationSuggestions.java</td>
      <td>GetGeographicalIndicationSuggestionsPort</td>
      <td>agSupportService</td>
      <td>AgSupportServiceImpl: 1 WebClient file(s)</td>
      <td>AgSupportServiceImpl</td>
    </tr>
    <tr>
      <td>GetMyDetails.java</td>
      <td>GetMyDetailsPort</td>
      <td>userProfileService</td>
      <td>UserProfileServiceImpl: 1 WebClient file(s)</td>
      <td>UserProfileServiceImpl</td>
    </tr>
    <tr>
      <td>GetUserDrafts.java</td>
      <td>GetUserDraftsPort</td>
      <td>formApplicationService</td>
      <td>FormApplicationServiceImpl: 1 WebClient file(s)</td>
      <td>FormApplicationServiceImpl</td>
    </tr>
    <tr>
      <td>ImportTrademark.java</td>
      <td>ImportTrademarkPort</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>PreAssessmentDomain.java</td>
      <td>PreAssessmentDomainPort</td>
      <td>domainsService</td>
      <td>DomainsServiceImpl: 1 WebClient file(s)</td>
      <td>DomainsServiceImpl</td>
    </tr>
    <tr>
      <td>RemoveRepresentation.java</td>
      <td>RemoveRepresentationPort</td>
      <td>formApplicationService</td>
      <td>FormApplicationServiceImpl: 1 WebClient file(s)</td>
      <td>FormApplicationServiceImpl</td>
    </tr>
    <tr>
      <td>SearchTrademark.java</td>
      <td>SearchTrademarkPort</td>
      <td>trademarkSearchService</td>
      <td>TrademarkSearchServiceImpl: 2 WebClient file(s)</td>
      <td>TrademarkSearchServiceImpl</td>
    </tr>
    <tr>
      <td>TextRecognition.java</td>
      <td>TextRecognitionPort</td>
      <td>textRecognitionService, documentRepositoryService</td>
      <td>DocumentRepositoryServiceImpl: 1 WebClient file(s)</td>
      <td>TextRecognitionServiceImpl, DocumentRepositoryServiceImpl</td>
    </tr>
    <tr>
      <td>UpdateForm.java</td>
      <td>UpdateFormPort</td>
      <td>formApplicationService</td>
      <td>FormApplicationServiceImpl: 1 WebClient file(s)</td>
      <td>FormApplicationServiceImpl</td>
    </tr>
    <tr>
      <td>UploadRepresentation.java</td>
      <td>UploadRepresentationPort</td>
      <td>textRecognitionService, documentRepositoryService</td>
      <td>DocumentRepositoryServiceImpl: 1 WebClient file(s)</td>
      <td>TextRecognitionServiceImpl, DocumentRepositoryServiceImpl</td>
    </tr>
    <tr>
      <td>ValidateApplicationUpdate.java</td>
      <td>ValidateApplicationUpdatePort</td>
      <td>formApplicationService</td>
      <td>FormApplicationServiceImpl: 1 WebClient file(s)</td>
      <td>FormApplicationServiceImpl</td>
    </tr>
    <tr>
      <td>CompareGoodsAndServices.java</td>
      <td>CompareGoodsAndServicesPort</td>
      <td>trademarkSearchService</td>
      <td>TrademarkSearchServiceImpl: 2 WebClient file(s)</td>
      <td>TrademarkSearchServiceImpl</td>
    </tr>
    <tr>
      <td>DownloadComparisonReport.java</td>
      <td>DownloadComparisonReportPort</td>
      <td>documentGeneratorService, formApplicationService, trademarkSearchService</td>
      <td>DocumentGeneratorServiceImpl: 1 WebClient file(s); FormApplicationServiceImpl: 1 WebClient file(s); TrademarkSearchServiceImpl: 2 WebClient file(s)</td>
      <td>DocumentGeneratorServiceImpl, FormApplicationServiceImpl, TrademarkSearchServiceImpl</td>
    </tr>
    <tr>
      <td>GetClassHeadingsByLanguage.java</td>
      <td>GetClassHeadingsByLanguagePort</td>
      <td>getClassHeadingsByLanguageService</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>GetPrefixes.java</td>
      <td>GetPrefixesPort</td>
      <td>getPrefixesService</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>GetSuggestedTerms.java</td>
      <td>GetSuggestedTermsPort</td>
      <td>getSuggestedTermsService</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>GetTaxonomyByLanguage.java</td>
      <td>GetTaxonomyByLanguagePort</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>ImportList.java</td>
      <td>ImportListPort</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>SearchPagedTerms.java</td>
      <td>SearchPagedTermsPort</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>TranslateClassification.java</td>
      <td>TranslateClassificationPort</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>ValidateClassification.java</td>
      <td>validation.ValidateClassificationPort</td>
      <td>validateTermsService</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>CSVFileManager.java</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>TextFileManager.java</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>
</div>
