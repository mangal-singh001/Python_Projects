import qrcode

# Taking UPI ID as a Input

upi_id = input("Enter your UPI Id = ")  

#  Format of payemnt url 
# upi://pay?pa=UPI_ID&pn=NAME&am=Amount&cu=CURRENCY&tn=MESSAGE
#  pa = upi id ,pn = recepient name ,am = amount ,cu = currency like in inr,tn = payment message , mc = merchant code are the parameters that are used for payment 


#  Defining the payemnt url based on the UPI id and the payment app
#  You can modify these URLs based on the payment apps you want to support 

phonepe_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
# paytm_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
# google_pay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'


#  Create QR code for each payment app

phonepe_qr = qrcode.make(phonepe_url)
# paytm_qr = qrcode.make(paytm_url)
# google_pay_qr = qrcode.make(google_pay_url)



# Save the qr code to image file (optional)

phonepe_qr.save('phonepe_qr.png')
# paytm_qr.save('paytm_qr.png')
# google_pay_qr.save('google_pay_qr.png')

# Display the QR codes (You may need to install PIL / PILLOW library)

phonepe_qr.show()
# paytm_qr.show()
# google_pay_qr.show()