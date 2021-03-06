# GetClassSchedulesRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_schedule_ids** | **list[int]** | The class schedule IDs.  &lt;br /&gt;Default: **all** | [optional] 
**end_date** | **datetime** | The end date of the range. Return any active enrollments that occur on or before this day.  &lt;br /&gt;Default: **StartDate** | [optional] 
**location_ids** | **list[int]** | The location IDs.   &lt;br /&gt;Default: **all** | [optional] 
**program_ids** | **list[int]** | The program IDs.   &lt;br /&gt;Default: **all** | [optional] 
**session_type_ids** | **list[int]** | The session type IDs.   &lt;br /&gt;Default: **all** | [optional] 
**staff_ids** | **list[int]** | The staff IDs.   &lt;br /&gt;Default: **all** | [optional] 
**start_date** | **datetime** | The start date of the range. Return any active enrollments that occur on or after this day.  &lt;br /&gt;Default: **today’s date** | [optional] 
**limit** | **int** | Number of results to include, defaults to 100 | [optional] 
**offset** | **int** | Page offset, defaults to 0. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


