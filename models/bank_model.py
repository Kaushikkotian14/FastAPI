from pydantic import BaseModel

class BankModel(BaseModel):
    account_number: str
    AccountHolder: str
    AadhaarNo: str
    phone: int
    email: str
    account_type: str
    address: str
    balance: float

class TransferModel(BaseModel):
    sender_phone: int
    receiver_phone: int
    amount: float