# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from firefly_iii_client.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from firefly_iii_client.model.account import Account
from firefly_iii_client.model.account_array import AccountArray
from firefly_iii_client.model.account_read import AccountRead
from firefly_iii_client.model.account_role_property import AccountRoleProperty
from firefly_iii_client.model.account_search_field_filter import AccountSearchFieldFilter
from firefly_iii_client.model.account_single import AccountSingle
from firefly_iii_client.model.account_store import AccountStore
from firefly_iii_client.model.account_type_filter import AccountTypeFilter
from firefly_iii_client.model.account_type_property import AccountTypeProperty
from firefly_iii_client.model.account_update import AccountUpdate
from firefly_iii_client.model.attachable_type import AttachableType
from firefly_iii_client.model.attachment import Attachment
from firefly_iii_client.model.attachment_array import AttachmentArray
from firefly_iii_client.model.attachment_read import AttachmentRead
from firefly_iii_client.model.attachment_single import AttachmentSingle
from firefly_iii_client.model.attachment_store import AttachmentStore
from firefly_iii_client.model.attachment_update import AttachmentUpdate
from firefly_iii_client.model.auto_budget_period import AutoBudgetPeriod
from firefly_iii_client.model.auto_budget_type import AutoBudgetType
from firefly_iii_client.model.autocomplete_account import AutocompleteAccount
from firefly_iii_client.model.autocomplete_account_array import AutocompleteAccountArray
from firefly_iii_client.model.autocomplete_bill import AutocompleteBill
from firefly_iii_client.model.autocomplete_bill_array import AutocompleteBillArray
from firefly_iii_client.model.autocomplete_budget import AutocompleteBudget
from firefly_iii_client.model.autocomplete_budget_array import AutocompleteBudgetArray
from firefly_iii_client.model.autocomplete_category import AutocompleteCategory
from firefly_iii_client.model.autocomplete_category_array import AutocompleteCategoryArray
from firefly_iii_client.model.autocomplete_currency import AutocompleteCurrency
from firefly_iii_client.model.autocomplete_currency_array import AutocompleteCurrencyArray
from firefly_iii_client.model.autocomplete_currency_code import AutocompleteCurrencyCode
from firefly_iii_client.model.autocomplete_currency_code_array import AutocompleteCurrencyCodeArray
from firefly_iii_client.model.autocomplete_object_group import AutocompleteObjectGroup
from firefly_iii_client.model.autocomplete_object_group_array import AutocompleteObjectGroupArray
from firefly_iii_client.model.autocomplete_piggy import AutocompletePiggy
from firefly_iii_client.model.autocomplete_piggy_array import AutocompletePiggyArray
from firefly_iii_client.model.autocomplete_piggy_balance import AutocompletePiggyBalance
from firefly_iii_client.model.autocomplete_piggy_balance_array import AutocompletePiggyBalanceArray
from firefly_iii_client.model.autocomplete_recurrence import AutocompleteRecurrence
from firefly_iii_client.model.autocomplete_recurrence_array import AutocompleteRecurrenceArray
from firefly_iii_client.model.autocomplete_rule import AutocompleteRule
from firefly_iii_client.model.autocomplete_rule_array import AutocompleteRuleArray
from firefly_iii_client.model.autocomplete_rule_group import AutocompleteRuleGroup
from firefly_iii_client.model.autocomplete_rule_group_array import AutocompleteRuleGroupArray
from firefly_iii_client.model.autocomplete_tag import AutocompleteTag
from firefly_iii_client.model.autocomplete_tag_array import AutocompleteTagArray
from firefly_iii_client.model.autocomplete_transaction import AutocompleteTransaction
from firefly_iii_client.model.autocomplete_transaction_array import AutocompleteTransactionArray
from firefly_iii_client.model.autocomplete_transaction_id import AutocompleteTransactionID
from firefly_iii_client.model.autocomplete_transaction_id_array import AutocompleteTransactionIDArray
from firefly_iii_client.model.autocomplete_transaction_type import AutocompleteTransactionType
from firefly_iii_client.model.autocomplete_transaction_type_array import AutocompleteTransactionTypeArray
from firefly_iii_client.model.available_budget import AvailableBudget
from firefly_iii_client.model.available_budget_array import AvailableBudgetArray
from firefly_iii_client.model.available_budget_read import AvailableBudgetRead
from firefly_iii_client.model.available_budget_single import AvailableBudgetSingle
from firefly_iii_client.model.available_budget_store import AvailableBudgetStore
from firefly_iii_client.model.available_budget_update import AvailableBudgetUpdate
from firefly_iii_client.model.basic_summary import BasicSummary
from firefly_iii_client.model.basic_summary_entry import BasicSummaryEntry
from firefly_iii_client.model.bill import Bill
from firefly_iii_client.model.bill_array import BillArray
from firefly_iii_client.model.bill_paid_dates import BillPaidDates
from firefly_iii_client.model.bill_read import BillRead
from firefly_iii_client.model.bill_repeat_frequency import BillRepeatFrequency
from firefly_iii_client.model.bill_single import BillSingle
from firefly_iii_client.model.bill_store import BillStore
from firefly_iii_client.model.bill_update import BillUpdate
from firefly_iii_client.model.budget import Budget
from firefly_iii_client.model.budget_array import BudgetArray
from firefly_iii_client.model.budget_limit import BudgetLimit
from firefly_iii_client.model.budget_limit_array import BudgetLimitArray
from firefly_iii_client.model.budget_limit_read import BudgetLimitRead
from firefly_iii_client.model.budget_limit_single import BudgetLimitSingle
from firefly_iii_client.model.budget_limit_store import BudgetLimitStore
from firefly_iii_client.model.budget_read import BudgetRead
from firefly_iii_client.model.budget_single import BudgetSingle
from firefly_iii_client.model.budget_spent import BudgetSpent
from firefly_iii_client.model.budget_store import BudgetStore
from firefly_iii_client.model.budget_update import BudgetUpdate
from firefly_iii_client.model.category import Category
from firefly_iii_client.model.category_array import CategoryArray
from firefly_iii_client.model.category_earned import CategoryEarned
from firefly_iii_client.model.category_read import CategoryRead
from firefly_iii_client.model.category_single import CategorySingle
from firefly_iii_client.model.category_spent import CategorySpent
from firefly_iii_client.model.category_store import CategoryStore
from firefly_iii_client.model.category_update import CategoryUpdate
from firefly_iii_client.model.chart_data_point import ChartDataPoint
from firefly_iii_client.model.chart_data_set import ChartDataSet
from firefly_iii_client.model.chart_line import ChartLine
from firefly_iii_client.model.config_value_filter import ConfigValueFilter
from firefly_iii_client.model.config_value_update_filter import ConfigValueUpdateFilter
from firefly_iii_client.model.configuration import Configuration
from firefly_iii_client.model.configuration_array import ConfigurationArray
from firefly_iii_client.model.configuration_single import ConfigurationSingle
from firefly_iii_client.model.configuration_update import ConfigurationUpdate
from firefly_iii_client.model.credit_card_type import CreditCardType
from firefly_iii_client.model.cron_result import CronResult
from firefly_iii_client.model.cron_result_row import CronResultRow
from firefly_iii_client.model.currency import Currency
from firefly_iii_client.model.currency_array import CurrencyArray
from firefly_iii_client.model.currency_read import CurrencyRead
from firefly_iii_client.model.currency_single import CurrencySingle
from firefly_iii_client.model.currency_store import CurrencyStore
from firefly_iii_client.model.currency_update import CurrencyUpdate
from firefly_iii_client.model.data_destroy_object import DataDestroyObject
from firefly_iii_client.model.export_file_filter import ExportFileFilter
from firefly_iii_client.model.insight_group import InsightGroup
from firefly_iii_client.model.insight_group_entry import InsightGroupEntry
from firefly_iii_client.model.insight_total import InsightTotal
from firefly_iii_client.model.insight_total_entry import InsightTotalEntry
from firefly_iii_client.model.insight_transfer import InsightTransfer
from firefly_iii_client.model.insight_transfer_entry import InsightTransferEntry
from firefly_iii_client.model.interest_period import InterestPeriod
from firefly_iii_client.model.liability_direction import LiabilityDirection
from firefly_iii_client.model.liability_type import LiabilityType
from firefly_iii_client.model.link_type import LinkType
from firefly_iii_client.model.link_type_array import LinkTypeArray
from firefly_iii_client.model.link_type_read import LinkTypeRead
from firefly_iii_client.model.link_type_single import LinkTypeSingle
from firefly_iii_client.model.link_type_store import LinkTypeStore
from firefly_iii_client.model.link_type_update import LinkTypeUpdate
from firefly_iii_client.model.meta import Meta
from firefly_iii_client.model.meta_pagination import MetaPagination
from firefly_iii_client.model.object_group import ObjectGroup
from firefly_iii_client.model.object_group_array import ObjectGroupArray
from firefly_iii_client.model.object_group_read import ObjectGroupRead
from firefly_iii_client.model.object_group_single import ObjectGroupSingle
from firefly_iii_client.model.object_group_update import ObjectGroupUpdate
from firefly_iii_client.model.object_link import ObjectLink
from firefly_iii_client.model.object_link0 import ObjectLink0
from firefly_iii_client.model.page_link import PageLink
from firefly_iii_client.model.piggy_bank import PiggyBank
from firefly_iii_client.model.piggy_bank_array import PiggyBankArray
from firefly_iii_client.model.piggy_bank_event import PiggyBankEvent
from firefly_iii_client.model.piggy_bank_event_array import PiggyBankEventArray
from firefly_iii_client.model.piggy_bank_event_read import PiggyBankEventRead
from firefly_iii_client.model.piggy_bank_read import PiggyBankRead
from firefly_iii_client.model.piggy_bank_single import PiggyBankSingle
from firefly_iii_client.model.piggy_bank_store import PiggyBankStore
from firefly_iii_client.model.piggy_bank_update import PiggyBankUpdate
from firefly_iii_client.model.polymorphic_property import PolymorphicProperty
from firefly_iii_client.model.preference import Preference
from firefly_iii_client.model.preference_array import PreferenceArray
from firefly_iii_client.model.preference_read import PreferenceRead
from firefly_iii_client.model.preference_single import PreferenceSingle
from firefly_iii_client.model.preference_update import PreferenceUpdate
from firefly_iii_client.model.recurrence import Recurrence
from firefly_iii_client.model.recurrence_array import RecurrenceArray
from firefly_iii_client.model.recurrence_read import RecurrenceRead
from firefly_iii_client.model.recurrence_repetition import RecurrenceRepetition
from firefly_iii_client.model.recurrence_repetition_store import RecurrenceRepetitionStore
from firefly_iii_client.model.recurrence_repetition_type import RecurrenceRepetitionType
from firefly_iii_client.model.recurrence_repetition_update import RecurrenceRepetitionUpdate
from firefly_iii_client.model.recurrence_single import RecurrenceSingle
from firefly_iii_client.model.recurrence_store import RecurrenceStore
from firefly_iii_client.model.recurrence_transaction import RecurrenceTransaction
from firefly_iii_client.model.recurrence_transaction_store import RecurrenceTransactionStore
from firefly_iii_client.model.recurrence_transaction_type import RecurrenceTransactionType
from firefly_iii_client.model.recurrence_transaction_update import RecurrenceTransactionUpdate
from firefly_iii_client.model.recurrence_update import RecurrenceUpdate
from firefly_iii_client.model.rule import Rule
from firefly_iii_client.model.rule_action import RuleAction
from firefly_iii_client.model.rule_action_keyword import RuleActionKeyword
from firefly_iii_client.model.rule_action_store import RuleActionStore
from firefly_iii_client.model.rule_action_update import RuleActionUpdate
from firefly_iii_client.model.rule_array import RuleArray
from firefly_iii_client.model.rule_group import RuleGroup
from firefly_iii_client.model.rule_group_array import RuleGroupArray
from firefly_iii_client.model.rule_group_read import RuleGroupRead
from firefly_iii_client.model.rule_group_single import RuleGroupSingle
from firefly_iii_client.model.rule_group_store import RuleGroupStore
from firefly_iii_client.model.rule_group_update import RuleGroupUpdate
from firefly_iii_client.model.rule_read import RuleRead
from firefly_iii_client.model.rule_single import RuleSingle
from firefly_iii_client.model.rule_store import RuleStore
from firefly_iii_client.model.rule_trigger import RuleTrigger
from firefly_iii_client.model.rule_trigger_keyword import RuleTriggerKeyword
from firefly_iii_client.model.rule_trigger_store import RuleTriggerStore
from firefly_iii_client.model.rule_trigger_type import RuleTriggerType
from firefly_iii_client.model.rule_trigger_update import RuleTriggerUpdate
from firefly_iii_client.model.rule_update import RuleUpdate
from firefly_iii_client.model.short_account_type_property import ShortAccountTypeProperty
from firefly_iii_client.model.string_array import StringArray
from firefly_iii_client.model.system_info import SystemInfo
from firefly_iii_client.model.system_info_data import SystemInfoData
from firefly_iii_client.model.tag_array import TagArray
from firefly_iii_client.model.tag_model import TagModel
from firefly_iii_client.model.tag_model_store import TagModelStore
from firefly_iii_client.model.tag_model_update import TagModelUpdate
from firefly_iii_client.model.tag_read import TagRead
from firefly_iii_client.model.tag_single import TagSingle
from firefly_iii_client.model.transaction import Transaction
from firefly_iii_client.model.transaction_array import TransactionArray
from firefly_iii_client.model.transaction_link import TransactionLink
from firefly_iii_client.model.transaction_link_array import TransactionLinkArray
from firefly_iii_client.model.transaction_link_read import TransactionLinkRead
from firefly_iii_client.model.transaction_link_single import TransactionLinkSingle
from firefly_iii_client.model.transaction_link_store import TransactionLinkStore
from firefly_iii_client.model.transaction_link_update import TransactionLinkUpdate
from firefly_iii_client.model.transaction_read import TransactionRead
from firefly_iii_client.model.transaction_single import TransactionSingle
from firefly_iii_client.model.transaction_split import TransactionSplit
from firefly_iii_client.model.transaction_split_store import TransactionSplitStore
from firefly_iii_client.model.transaction_split_update import TransactionSplitUpdate
from firefly_iii_client.model.transaction_store import TransactionStore
from firefly_iii_client.model.transaction_type_filter import TransactionTypeFilter
from firefly_iii_client.model.transaction_type_property import TransactionTypeProperty
from firefly_iii_client.model.transaction_update import TransactionUpdate
from firefly_iii_client.model.user import User
from firefly_iii_client.model.user_array import UserArray
from firefly_iii_client.model.user_blocked_code_property import UserBlockedCodeProperty
from firefly_iii_client.model.user_read import UserRead
from firefly_iii_client.model.user_role_property import UserRoleProperty
from firefly_iii_client.model.user_single import UserSingle
from firefly_iii_client.model.validation_error import ValidationError
from firefly_iii_client.model.validation_error_errors import ValidationErrorErrors
from firefly_iii_client.model.webhook import Webhook
from firefly_iii_client.model.webhook_array import WebhookArray
from firefly_iii_client.model.webhook_attempt import WebhookAttempt
from firefly_iii_client.model.webhook_attempt_array import WebhookAttemptArray
from firefly_iii_client.model.webhook_attempt_read import WebhookAttemptRead
from firefly_iii_client.model.webhook_attempt_single import WebhookAttemptSingle
from firefly_iii_client.model.webhook_delivery import WebhookDelivery
from firefly_iii_client.model.webhook_message import WebhookMessage
from firefly_iii_client.model.webhook_message_array import WebhookMessageArray
from firefly_iii_client.model.webhook_message_read import WebhookMessageRead
from firefly_iii_client.model.webhook_message_single import WebhookMessageSingle
from firefly_iii_client.model.webhook_read import WebhookRead
from firefly_iii_client.model.webhook_response import WebhookResponse
from firefly_iii_client.model.webhook_single import WebhookSingle
from firefly_iii_client.model.webhook_store import WebhookStore
from firefly_iii_client.model.webhook_trigger import WebhookTrigger
from firefly_iii_client.model.webhook_update import WebhookUpdate