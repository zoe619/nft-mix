#!/usr/bin/python3
from brownie import AdvancedCollectible, accounts, network, config
from scripts.helpful_scripts import fund_with_link


def main():
    dev = accounts.add(config["wallets"]["from_key"])
    print(network.show_active())
    print(dev)
    # publish_source = True if os.getenv("ETHERSCAN_TOKEN") else False # Currently having an issue with this
    publish_source=True
    advanced_collectible = AdvancedCollectible.deploy(
        '0xb3dCcb4Cf7a26f6cf6B120Cf5A73875B7BBc655B',
        '0x01be23585060835e02b77ef475b0cc51aa1e0709',
        '0x2ed0feb3e7fd2022120aa84fab1945545a9f2ffc9076fd6156fa96eaff4c1311',
        {"from": dev},
        publish_source= publish_source
        
    )
    fund_with_link(advanced_collectible.address)
    return advanced_collectible
