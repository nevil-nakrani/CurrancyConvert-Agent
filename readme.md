# Currency Converter with LLM Tool Calling

This project demonstrates how to use LangChain's tool calling capabilities with Google Generative AI to perform currency conversion using real-time exchange rates.

## Features

- Fetches live currency conversion rates using [ExchangeRate-API](https://www.exchangerate-api.com/).
- Uses LangChain's tool calling to chain function calls for multi-step reasoning.
- Converts currency values based on user queries.
- Speaks the result using `pyttsx3` text-to-speech.

## Requirements

- Python 3.9+
- [requirements.txt](requirements.txt) dependencies:
  - langchain
  - langchain-google-genai
  - python-dotenv
  - pyttsx3
  - requests

## Setup

1. Clone the repository.
2. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```
3. Set up your `.env` file with any required environment variables (e.g., API keys).

## Usage

Run the main script:

```sh
python ToolCalling.py
```

You will be prompted with a sample query ("How much is 100 USD in INR?"). The script will:
- Call the exchange rate API,
- Calculate the converted amount,
- Print and speak the result.

## File Structure

- `ToolCalling.py`: Main script with tool definitions and LLM invocation.
- `requirements.txt`: Python dependencies.
- `.env`: Environment variables (not included in version control).

## Notes

- Make sure your API key for ExchangeRate-API is valid and set in the script or `.env`.
- You can modify the prompt or extend the tools for more currencies or additional features.

## License

MIT License
