from aleph_client.synchronous import get_posts
from  aleph_client.chains.ethereum import ETHAccount,get_fallback_account
from aleph_client.synchronous import  create_post,create_aggregate, fetch_aggregate
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
        return account

    def ConnectWithAccount(self):
        Key = ETHAccount(self.key)
        print("Key",Key )
        return Key

    def CreateResource(self, account_Key):
        response = create_post(account_Key,{'content':'Test'},post_type = 'test_type',channel = 'My_Channel')
        return response



    '''Aggregate objects allow you to store key-value pairs associated with an address. 
    Keys are strings and values are objects.'''
    def CreateAggregate(self, account_Key  ,key:str,data: dict):



        # This takes 7 parameters 3 are mandatory and  4 are optional
        # 1:accountkey  sender account
        # 2:key  this can be mutated
        # 3: content  this is the value of the save for the key

        '''This is  optional'''
        # 4 : address
        ''' address takes string  Address the aggregate should be associated with
         One can pass a different address than the account address to update the aggregate 
         for this target address'''
        # 5:  channel  Channel of the message ideally one application used the one channel
        # 6 : Session  Set it as a default :None
        # 7 : api server which is by default "https://api2.aleph.im"

        AggregatedMessage =  create_aggregate(account_Key,key,data, channel = "MY_Channel")
        return AggregatedMessage

    def FetchOneAggregate(self,account):


       # '''Return the content value of the query key for an address '''
        # If no aggregate for the address and the key is found ,null will be returned
        # It takes 4 arguments  2 are Required and 2 is optional
        # 1 :address  the chain address the aggregate was created for
        # 2 : key  the key the aggregated was created here I have created with names
        #Optional para
        # 3 session Default
        # api_server which is default "https://api2.aleph.im
        fetchOneAggregate = fetch_aggregate(account.get_address(),'names')
        return fetchOneAggregate

    def UpdateKey(self,account,Key_name , data):
        ''' Use the  create_aggregate  endpoint to update the specific key value from an existing Aggregate   '''
        # Since creating an aggregate message mutates the value of the specific key, if the key exist the
        # Object value will be updated(mutated) with the object you are saving

        UpdateAgg = create_aggregate(account, Key_name, data, channel ='MY_CHANNEL')
        return UpdateAgg















if __name__ == '__main__':
    Al_Ob = Aleph(chats='chat',refs='hall',key='7735788a8c4283da1851c3a034237ccd9a283babc60fd5afd151a9837c4625d1')
    Al_Ob.check()
    key = Al_Ob.ConnectWithAccount()
    key2= Al_Ob.ConnectWithoutPrivate()

    print("Key     :",key.get_address())



    created_Resources = Al_Ob.CreateResource(key2)
    names ={ 'akram':112 ,'Aslam':1123, 'Naem': 145}
    createdAggregatedMessage =  Al_Ob.CreateAggregate(account_Key=key,key = 'names',data = names )

    print("Aggreted Message is here     :", createdAggregatedMessage)
    RetrieveOneRecord = Al_Ob.FetchOneAggregate(account=key)
    print ("Retrieved Single Record     :    ", RetrieveOneRecord)
    updatenames = {'Julian ':1834 ,'akram':22}
    UpdateAggOb = Al_Ob.UpdateKey(account = key , Key_name = 'names' , data= updatenames)
    print("UpdatedAgg:  ", UpdateAggOb)





