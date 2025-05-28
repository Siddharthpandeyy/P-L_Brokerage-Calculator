# Write code below 💖

  
Buy=float(input("Enter Buy Price: "))
Sell=float(input("Enter Sell Price: "))
Qty=int(input("Enter No of Qty:"))
Rate=float(input("Enter Brokerage rate:"))


def profit_or_loss(Buy,Sell,Qty,Rate):
  brok=((Buy+Sell)*Qty)*Rate 
  tot=((Sell*Qty)-(Buy*Qty))-brok
  Per=(tot/(Buy*Qty))*100
  
  if tot>0:
    return f"Profit of ${ tot:.2f}.incl Brokerage| Gain of {Per:.2f}% | Brokerage: ${brok:.2f}"
  elif tot<0:
    return f"Loss of $ {tot:.2f}.incl Brokerage | Loss of {Per:.2f}% | Brokerage: ${brok:.2f}"
  else:
    return("No Gain")

print(profit_or_loss(Buy,Sell,Qty,Rate))