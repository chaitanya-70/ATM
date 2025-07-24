class Node: 
  def _init_(self,transaction_type,amount):
    self.type=transaction_type
    self.amount=amount
    self.next=None

class TransactionHistory:
  def _init_(self):
    self.head=None

  def add_transaction(self,transaction_type,amount):
    nn=Node(transaction_type,amount) 
    if not self.head:
      self.head=nn
    else:
      current=self.head
      while current.next:
        current=current.next
      current.next = nn 
    print(f"{transaction_type} of rs.{amount} added to history") 

  def display_history(self):
    if not self.head:
      print(
          "No transaction history.")
      return
    print("\n Transaction History:")
    current=self.head
    count=1
    while current:
      print(f"{count}. {current.type} of rs.{current.amount}") 
      current=current.next
      count+=1
history=TransactionHistory()
while True:
  print("\n ........ATM Transaction menu...........")
  print("1.deposit")
  print("2. WithDraw")
  print("3.history")
  print("4.Exit")
  choice=input("Enter your choice:")
  if choice=='1':
    amount=int(input("Enter amount to deposit:"))
    history.add_transaction("deposit",amount) 
  elif choice=='2':
    amount=float(input("Enter amount to withdraw:"))
    history.add_transaction("withdraw",amount)
  elif choice=='3':
    history.display_history()
  elif choice=='4':
    print("exiting the option....")
    break 
  else:
    print("chose only in 1,2,3,4........")
