from pipedrive import Pipedrive
pd = Pipedrive('dc8fe731bb412373b21482cdb0a8a73c265afb18')
                       # ^ insert API token
                       
EAAR = pd.deals.get(id=693) ## parse info from given field 

Current_value = float(EAAR.value) ## convert value to decimal

print 'Previous value was ', Current_value

New_value = Current_value * 0.96
print 'New Value is ', New_value

pd.deals.put({
    "id":693,
    "value":9})

EAAR2 = pd.deals.get(id=693)

print EAAR2.value

'''
 dc8fe731bb412373b21482cdb0a8a73c265afb18 (API token)
 936fba7d7033c7e1a0369820f93991f5a3849df7 (field_key)  12467 (field_id)
 693 (deal_id)
 "Estimated Avg Annual Revenue" (field_name)
'''
