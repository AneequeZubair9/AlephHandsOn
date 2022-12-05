from aleph_client.synchronous import get_posts
from  aleph_client.chains.ethereum import ETHAccount,get_fallback_account
from aleph_client.synchronous import  create_post
class Aleph:

    def __init__(self,chats,refs,key):

        self.chats = chats
        self.refs  = refs
        self.key = key

    def check(self):
        check = get_posts(types=[self.chats],refs =[self.refs],pagination = 3)
        for key,value in check.items():
            print("Key  ",key  ,"Value :",value)


    def ConnectWithoutPrivate(self):
        account = get_fallback_account()
        return dir(account)

    def ConnectWithAccount(self):
        Key = ETHAccount(self.key)
        print("Key",Key )
        return Key








if __name__ == '__main__':
    Al_Ob = Aleph(chats='chat',refs='hall',key='7735788a8c4283da1851c3a034237ccd9a283babc60fd5afd151a9837c4625d1')
    Al_Ob.check()
    Al_Ob.ConnectWithAccount()





