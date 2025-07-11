from repositories.bank_repository import insert_bank_account, find_bank_by_phone, update_bank_balance
import random
 
def create_bank_account_service(account):
    if find_bank_by_phone(account.phone):
        return {"error": "Phone already registered"}
 
    account_number = str(random.randint(100000000000, 999999999999))
    data = {
        "account_number": account_number,
        "AccountHolder": account.name,
        "AadhaarNo": account.aadhar_no,
        "phone": account.phone,
        "email": account.email,
        "account_type": account.account_type,
        "address": account.address,
        "balance": account.balance,
    }
    insert_bank_account(data)
    return {"msg": "Bank account created", "account_number": account_number}

def transfer_money_service(sender_phone: int, receiver_phone: int, amount: float):
    
    sender_account = find_bank_by_phone(sender_phone)
    receiver_account = find_bank_by_phone(receiver_phone)

    if not sender_account:
        return {"error": "Sender account not found"}
    if not receiver_account:
        return {"error": "Receiver account not found"}
    if sender_phone == receiver_phone:
        return {"error": "Cannot transfer to same account"}
    if sender_account["balance"] < amount:
        return {"error": "Insufficient balance"}
    if amount <= 0:
        return {"error": "Invalid transfer amount"}

   
    update_bank_balance(sender_phone, sender_account["balance"] - amount)
    update_bank_balance(receiver_phone, receiver_account["balance"] + amount)

    return {"msg": "Transfer successful", "amount": amount}