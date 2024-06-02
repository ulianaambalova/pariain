    for wallet in wallets:
        # Retrieve wallet name.
        wallet_name = wallet.name
        print("Wallet name: {}".format(wallet_name))

        # Retrieve wallet balance.
        balance = wallet.balance
        print("Wallet balance: {}".format(balance))

        # Retrieve wallet address.
        address = wallet.address
        print("Wallet address: {}".format(address))  
