from brownie import accounts, config, SimpleStorage, network
# import os
import time

print("\nCreate decentralised storage system.\n")
time.sleep(5)


def deploy_simple_storage():
    account = get_account()
    simple_storage = SimpleStorage.deploy({"from": account})  # Trasnact Call
    # print(simple_storage)
    stored_value = simple_storage.retrieve()
    time.sleep(5)
    print(stored_value)
    #   transaction = simple_storage.store()
    transaction = simple_storage.store(15, {"from": account})
    transaction.wait(1)
    updated_stored_value = simple_storage.retrieve()
    time.sleep(5)
    print(updated_stored_value)
    print("Storage System Created!")
    time.sleep(5)

    #   account = accounts.load("<account_name>")
    #   print(account)
    #   account = accounts.add(os.getenv("PRIVATE_KEY"))
    #   print(account)
    #   account = accounts.add(config["wallets"]["from_key"])
    #   print(account)


def get_account():
    if network.show_active() == 'development':
        return accounts[0]
    else:
        return accounts.add(config["wallets"]['from_key'])


def main():
    deploy_simple_storage()
