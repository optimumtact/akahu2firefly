# WebhookUpdate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | Boolean to indicate if the webhook is active | [optional] 
**delivery** | [**WebhookDelivery**](WebhookDelivery.md) |  | [optional] 
**response** | [**WebhookResponse**](WebhookResponse.md) |  | [optional] 
**secret** | **str** | A 24-character secret for the webhook. It&#39;s generated by Firefly III when saving a new webhook. If you submit a new secret through the PUT endpoint it will generate a new secret for the selected webhook, a new secret bearing no relation to whatever you just submitted. | [optional] 
**title** | **str** | A title for the webhook for easy recognition. | [optional] 
**trigger** | [**WebhookTrigger**](WebhookTrigger.md) |  | [optional] 
**url** | **str** | The URL of the webhook. Has to start with &#x60;https&#x60;. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

