from datetime import datetime
from enum import StrEnum
from pydantic import BaseModel, ConfigDict, Field


class OperationStatus(StrEnum):
    COMPLETED = "COMPLETED"
    PENDING = "PENDING"
    FAILED = "FAILED"


class OperationType(StrEnum):
    TOP_UP = "TOP_UP"
    PURCHASE = "PURCHASE"
    TRANSFER = "TRANSFER"
    CASHBACK = "CASHBACK"
    FEE = "FEE"
    BILL_PAYMENT = "BILL_PAYMENT"
    CASH_WITHDRAWAL = "CASH_WITHDRAWAL"


class OperationSchema(BaseModel):
    id: str
    type: OperationType
    status: OperationStatus
    amount: float
    category: str
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")
    created_at: datetime = Field(alias="createdAt")


class OperationReceiptSchema(BaseModel):
    url: str
    document: str


class OperationsSummarySchema(BaseModel):
    spent_amount: float = Field(alias="spentAmount")
    received_amount: float = Field(alias="receivedAmount")
    cashback_amount: float = Field(alias="cashbackAmount")


class GetOperationResponseSchema(BaseModel):
    operation: OperationSchema


class GetOperationReceiptResponseSchema(BaseModel):
    receipt: OperationReceiptSchema


class GetOperationsResponseSchema(BaseModel):
    operations: list[OperationSchema]


class GetOperationsSummaryResponseSchema(BaseModel):
    summary: OperationsSummarySchema


class GetOperationsQuerySchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    account_id: str = Field(alias="accountId")


class GetOperationsSummaryQuerySchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    account_id: str = Field(alias="accountId")


class MakeOperationRequestSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    status: OperationStatus
    amount: float
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")


class MakeFeeOperationRequestSchema(MakeOperationRequestSchema):
    pass


class MakeTopUpOperationRequestSchema(MakeOperationRequestSchema):
    pass


class MakeCashbackOperationRequestSchema(MakeOperationRequestSchema):
    pass


class MakeTransferOperationRequestSchema(MakeOperationRequestSchema):
    pass


class MakePurchaseOperationRequestSchema(MakeOperationRequestSchema):
    category: str


class MakeBillPaymentOperationRequestSchema(MakeOperationRequestSchema):
    pass


class MakeCashWithdrawalOperationRequestSchema(MakeOperationRequestSchema):
    pass


class MakeFeeOperationResponseSchema(BaseModel):
    operation: OperationSchema


class MakeTopUpOperationResponseSchema(BaseModel):
    operation: OperationSchema


class MakeCashbackOperationResponseSchema(BaseModel):
    operation: OperationSchema


class MakeTransferOperationResponseSchema(BaseModel):
    operation: OperationSchema


class MakePurchaseOperationResponseSchema(BaseModel):
    operation: OperationSchema


class MakeBillPaymentOperationResponseSchema(BaseModel):
    operation: OperationSchema


class MakeCashWithdrawalOperationResponseSchema(BaseModel):
    operation: OperationSchema

