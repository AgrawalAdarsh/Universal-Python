def demon(a,b):
	print("Demon at work!")
	print("Ans of a*b= ",(a*b))
	def subdemo(b,c):
		print("Sub function called: Demon underling subdemo at work")
		print("Ans of b/c= ",(b/c))
	print("Demon function orders(calling) subdemon")
	subdemo(10,2)
demon(20,10)
