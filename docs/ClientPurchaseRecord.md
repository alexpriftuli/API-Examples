# ClientPurchaseRecord

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sale** | [**Sale**](Sale.md) | Contains details about the sale and payment for a purchase event. | [optional] 
**description** | **str** | The item name and description. | [optional] 
**account_payment** | **bool** | If &#x60;true&#x60;, the item was a payment credited to an account. | [optional] 
**price** | **float** | The item&#39;s price before taxes and discounts. | [optional] 
**amount_paid** | **float** | The amount paid for the item. | [optional] 
**discount** | **float** | The discount amount that was applied to the item. | [optional] 
**tax** | **float** | The amount of tax that was applied to the item. | [optional] 
**returned** | **bool** | The return status of the item. If &#x60;true&#x60;, this item was returned. | [optional] 
**quantity** | **int** | The quantity of the item purchased. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


