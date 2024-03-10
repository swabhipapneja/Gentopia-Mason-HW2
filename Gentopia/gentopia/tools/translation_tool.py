from typing import Any, Optional, Type
from gentopia.tools.basetool import BaseTool, BaseModel, Field
from transformers import MarianMTModel, MarianTokenizer

class TranslationParameters(BaseModel):
    source_language: str = Field(..., description="Source language code (e.g., 'en' for English)")
    target_language: str = Field(..., description="Target language code (e.g., 'fr' for French)")
    text_to_translate: str = Field(..., description="Text to be translated")

# class for Translation functionality
class TranslationTool(BaseTool):
    """Tool for language translation"""
    name = "translation_tool"
    description = "A tool for language translation that translates text from one language to another."

    args_schema: Optional[Type[BaseModel]] = TranslationParameters

    # Method to translate text
    def _run(self, source_language: str, target_language: str, text_to_translate: str) -> str:
        # Defining a model and tokenizer using MarianMT library
        model = f'Helsinki-NLP/opus-mt-{source_language}-{target_language}'
        tokenizer = MarianTokenizer.from_pretrained(model)
        model = MarianMTModel.from_pretrained(model)
        # tokenizing input
        input_tokens = tokenizer.encode(text_to_translate, return_tensors='pt')
        # translating the tokens
        output_tokens = model.generate(input_tokens)
        # detokenizing the translated tokens
        translated_text = tokenizer.decode(output_tokens[0], skip_special_tokens=True)
        return translated_text

    async def _arun(self, *args: Any, **kwargs: Any) -> Any:
        raise NotImplementedError("Asynchronous execution not implemented.")

if __name__ == "__main__":
    # Example translation
    translation_params = TranslationParameters(
        source_language="en",
        target_language="fr",
        text_to_translate="Hello, how are you?"
    )

    # creating an instance object of the TranslationTool class
    translation_tool = TranslationTool()
    translated_text = translation_tool._run(**translation_params.dict())
    # printing the translated output
    print(f"Translated text: {translated_text}")
