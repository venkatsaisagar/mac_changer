import subprocess

print(r""" 
  _      _     _ _ _ _      _      _     _    _         ____       _________
 \ \    / /   |  _ _ _|    |  \   | |   | |  / /       /    \     |___   ___|
  \ \  / /    | |_ _ _     | |\\  | |   | | / /       /  /\  \        | |
   \ \/ /     |  _ _ _|    | | \\ | |   | |/_/\      |  /__\  |       | |
    \  /      | |_ _ _     | |  \\| |   | |  \ \     | |    | |       | |
     \/       |_ _ _ _|    |_|   \ _|   |_|   \_\    |_|    |_|       |_|

DINDI VENKAT SAI SAGAR... ... ...
""")

if __name__=="__main__":
	interface="eth0"
	new_addres=input("please enter your new mac address:")

	print("shutting down the interface")
	subprocess.run(['ifconfig','eth0','down'])

	print("changing the interface hw address of",interface,'to',new_addres)
	subprocess.run(['ifconfig',interface,'hw','ether',new_addres])

	print('mac address changed to',new_addres)
	subprocess.run(['ifconfig',interface,'up'])

	print('network interface turned on.')


print('\n')
print("THANKS FOR USING MY TOOL :)")
print("YOU CAN REACH OUT TO ME BY :) ")
print("""
    _____
    | S |
    | A |
   _| G |_
   \  A  /
    \ R /
     \ /
      v
""")
print("venkatsaisagar.github@gmail.com")
