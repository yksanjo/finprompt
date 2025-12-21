"""
FinPrompt: Local LLM for Secure Financial Querying
"""

import ollama
import pandas as pd
import re
from typing import List, Dict
from loguru import logger


class FinPrompt:
    """Privacy-first financial assistant."""
    
    def __init__(self, model: str = "phi3:mini"):
        """Initialize FinPrompt."""
        self.model = model
        self.data: pd.DataFrame = None
    
    def load_csv(self, filepath: str):
        """Load financial data from CSV."""
        self.data = pd.read_csv(filepath)
        # Redact PII
        self._redact_pii()
        logger.info(f"Loaded {len(self.data)} transactions")
    
    def _redact_pii(self):
        """Redact personally identifiable information."""
        # Redact account numbers
        if 'account' in self.data.columns:
            self.data['account'] = self.data['account'].apply(
                lambda x: re.sub(r'\d', 'X', str(x)) if pd.notna(x) else x
            )
    
    def query(self, question: str) -> str:
        """Answer a question about financial data."""
        if self.data is None:
            return "No data loaded. Please import a CSV file first."
        
        # Generate summary of data
        summary = self._generate_summary()
        
        prompt = f"""You are a financial assistant analyzing transaction data.

Data Summary:
{summary}

User Question: {question}

Provide a helpful answer based on the data. Be specific and cite numbers when relevant.

Answer:"""
        
        try:
            response = ollama.generate(
                model=self.model,
                prompt=prompt
            )
            return response["response"]
        except Exception as e:
            logger.error(f"Error generating response: {e}")
            return f"Error: {str(e)}"
    
    def _generate_summary(self) -> str:
        """Generate summary of financial data."""
        if self.data is None or len(self.data) == 0:
            return "No transactions"
        
        summary = f"Total transactions: {len(self.data)}\n"
        
        if 'amount' in self.data.columns:
            total = self.data['amount'].sum()
            summary += f"Total amount: ${total:,.2f}\n"
        
        if 'date' in self.data.columns:
            dates = pd.to_datetime(self.data['date'], errors='coerce')
            summary += f"Date range: {dates.min()} to {dates.max()}\n"
        
        return summary


if __name__ == "__main__":
    fp = FinPrompt()
    # Example usage
    # fp.load_csv("transactions.csv")
    # answer = fp.query("What's my total spending?")
    # print(answer)

