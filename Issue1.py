#!/usr/bin/python

from pipedrive import Pipedrive
pd = Pipedrive('pipedrive_token')
                       # ^ insert API token
                       

 ## parse info from given field 

Deal = pd.deals.get(id=693)
    
EAAR = Deal.data['936fba7d7033c7e1a0369820f93991f5a3849df7']

current_value = Deal.value
current_eaar = EAAR 

## convert value to decimal

print 'EAAR was ', current_eaar

new_value = current_eaar * 0.0096

print 'Value was ', current_value
print 'Value should now be ', new_value

pd.deals.put(id=693,data={
    "value":new_value})


## Double checking the put statement
Deal2 = pd.deals.get(id=693)
EAAR2 = Deal2.value

print 'Value is now ', EAAR2


'''
 dc8fe731bb412373b21482cdb0a8a73c265afb18 (API token)
 936fba7d7033c7e1a0369820f93991f5a3849df7 (field_key)  12467 (field_id)
 693 (deal_id)
 "Estimated Avg Annual Revenue" (field_name)
'''
