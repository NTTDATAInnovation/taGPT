from config import MODEL, TEMPERATURE, N, IBM_CLOUD_API_KEY, WATSONX_AI_ENDPOINT, PROJECT_ID
from apis.abstract import AbstractAPICaller

try:
    # from langchain import PromptTemplate
    from langchain.chains import LLMChain
    # from langchain.document_loaders import PyPDFLoader
    # from langchain.indexes import VectorstoreIndexCreator #vectorize db index with chromadb
    # from langchain.embeddings import HuggingFaceEmbeddings #for using HugginFace embedding models
    # from langchain.text_splitter import CharacterTextSplitter #text splitter
    # from langchain.llms.base import LLM
    # from langchain.llms.utils import enforce_stop_tokens
except ImportError:
    raise ImportError("Could not import langchain: Please install ibm-generative-ai[langchain] extension.")

from ibm_watson_machine_learning.foundation_models.utils.enums import ModelTypes
from ibm_watson_machine_learning.foundation_models import Model
from ibm_watson_machine_learning.metanames import GenTextParamsMetaNames as GenParams
from ibm_watson_machine_learning.foundation_models.utils.enums import DecodingMethods
from ibm_watson_machine_learning.foundation_models.extensions.langchain import WatsonxLLM


class WATSONXCaller(AbstractAPICaller):

    @staticmethod
    def query(prompt, text):

        params = {
            GenParams.DECODING_METHOD: DecodingMethods.GREEDY,
            GenParams.MIN_NEW_TOKENS: 1,
            GenParams.MAX_NEW_TOKENS: 100,
            # GenParams.RANDOM_SEED: 42,
            # GenParams.TEMPERATURE: 0.5,
            # GenParams.TOP_K: 50,
            # GenParams.TOP_P:1
        }

        creds = {
            "url": WATSONX_AI_ENDPOINT,
            "apikey": IBM_CLOUD_API_KEY 
        }

        wxModel = Model(
        model_id=ModelTypes.FLAN_UL2, 
        params=params, 
        credentials=creds,
        project_id=PROJECT_ID)

        llm_model = WatsonxLLM(model=wxModel)
        chain = LLMChain(llm=llm_model, prompt=prompt)       
        
        return chain.run(text)
    
