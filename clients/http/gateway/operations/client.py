from typing import TypedDict

from httpx import Response, QueryParams

from clients.http.client import HTTPClient

from clients.http.gateway.client import build_gateway_http_client


class GetOperationsQueryDict(TypedDict):
    """
    Структура query параметров запроса для получения списка операций по счёту.
    """
    accountId: str


class GetOperationsSummaryQueryDict(TypedDict):
    """
    Структура query параметров запроса для получения статистики по операциям счёта.
    """
    accountId: str


class MakeOperationRequestDict(TypedDict):
    """
    Базовая структура тела запроса для создания финансовой операции.
    """
    status: str
    amount: float
    cardId: str
    accountId: str


class MakeFeeOperationRequestDict(MakeOperationRequestDict):
    """
    Структура запроса для создания операции комиссии.
    """
    pass


class MakeTopUpOperationRequestDict(MakeOperationRequestDict):
    """
    Структура запроса для создания операции пополнения.
    """
    pass


class MakeCashbackOperationRequestDict(MakeOperationRequestDict):
    """
    Структура запроса для создания операции кэшбэка.
    """
    pass


class MakeTransferOperationRequestDict(MakeOperationRequestDict):
    """
    Структура запроса для создания операции перевода.
    """
    pass


class MakePurchaseOperationRequestDict(MakeOperationRequestDict):
    """
    Структура запроса для создания операции покупки.

    Дополнительное поле:
    - category: категория покупки.
    """
    category: str


class MakeBillPaymentOperationRequestDict(MakeOperationRequestDict):
    """
    Структура запроса для создания операции оплаты по счёту.
    """
    pass


class MakeCashWithdrawalOperationRequestDict(MakeOperationRequestDict):
    """
    Структура запроса для создания операции снятия наличных.
    """
    pass


class OperationDict(TypedDict):
    """
    Описание структуры одной финансовой операции.
    """
    id: str
    type: str
    status: str
    amount: float
    cardId: str
    category: str
    createdAt: str
    accountId: str


class OperationReceiptDict(TypedDict):
    """
    Описание структуры чека по операции.
    """
    url: str
    document: str


class OperationsSummaryDict(TypedDict):
    """
    Описание структуры сводной статистики по операциям.
    """
    spentAmount: float
    receivedAmount: float
    cashbackAmount: float


class GetOperationResponseDict(TypedDict):
    """
    Структура ответа получения информации об одной операции.
    """
    operation: OperationDict


class GetOperationReceiptResponseDict(TypedDict):
    """
    Структура ответа получения чека операции.
    """
    receipt: OperationReceiptDict


class GetOperationsResponseDict(TypedDict):
    """
    Структура ответа получения списка операций по счёту.
    """
    operations: list[OperationDict]


class GetOperationsSummaryResponseDict(TypedDict):
    """
    Структура ответа получения статистики по операциям.
    """
    summary: OperationsSummaryDict


class MakeFeeOperationResponseDict(TypedDict):
    """
    Структура ответа создания операции комиссии.
    """
    operation: OperationDict


class MakeTopUpOperationResponseDict(TypedDict):
    """
    Структура ответа создания операции пополнения.
    """
    operation: OperationDict


class MakeCashbackOperationResponseDict(TypedDict):
    """
    Структура ответа создания операции кэшбэка.
    """
    operation: OperationDict


class MakeTransferOperationResponseDict(TypedDict):
    """
    Структура ответа создания операции перевода.
    """
    operation: OperationDict


class MakePurchaseOperationResponseDict(TypedDict):
    """
    Структура ответа создания операции покупки.
    """
    operation: OperationDict


class MakeBillPaymentOperationResponseDict(TypedDict):
    """
    Структура ответа создания операции оплаты по счету.
    """
    operation: OperationDict


class MakeCashWithdrawalOperationResponseDict(TypedDict):
    """
    Структура ответа создания операции снятия наличных.
    """
    operation: OperationDict


class OperationsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/operations сервиса http-gateway.
    """

    def get_operation_api(self, operation_id: str) -> Response:
        """
        Выполняет GET-запрос для получения информации об операции по её ID.

        :param operation_id: Идентификатор операции.
        :return: Объект httpx.Response с данными об операции.
        """
        return self.get(f"/api/v1/operations/{operation_id}")

    def get_operation_receipt_api(self, operation_id: str) -> Response:
        """
        Выполняет GET-запрос для получения чека по операции.

        :param operation_id: Идентификатор операции.
        :return: Объект httpx.Response с данными чека.
        """
        return self.get(f"/api/v1/operations/operation-receipt/{operation_id}")

    def get_operations_api(self, query: GetOperationsQueryDict) -> Response:
        """
        Получает список операций по счёту.

        :param query: Словарь с параметром accountId.
        :return: Объект httpx.Response с операциями по счёту.
        """
        return self.get("/api/v1/operations", params=QueryParams(**query))

    def get_operations_summary_api(self, query: GetOperationsSummaryQueryDict) -> Response:
        """
        Получает сводную статистику операций по счёту.

        :param query: Словарь с параметром accountId.
        :return: Объект httpx.Response с агрегированной информацией.
        """
        return self.get("/api/v1/operations/operations-summary", params=QueryParams(**query))

    def make_fee_operation_api(self, request: MakeFeeOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для создания операции комиссии.

        :param request: Словарь с данными для создания операции.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-fee-operation", json=request)

    def make_top_up_operation_api(self, request: MakeTopUpOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для создания операции пополнения.

        :param request: Словарь с данными для создания операции.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-top-up-operation", json=request)

    def make_cashback_operation_api(self, request: MakeCashbackOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для создания операции кэшбэка.

        :param request: Словарь с данными для создания операции.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-cashback-operation", json=request)

    def make_transfer_operation_api(self, request: MakeTransferOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для создания операции перевода.

        :param request: Словарь с данными для создания операции.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-transfer-operation", json=request)

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для создания операции покупки.

        :param request: Словарь со специальными данными покупки (включая category).
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-purchase-operation", json=request)

    def make_bill_payment_operation_api(self, request: MakeBillPaymentOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для создания операции оплаты по счету.

        :param request: Словарь с данными для создания операции.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-bill-payment-operation", json=request)

    def make_cash_withdrawal_operation_api(self, request: MakeCashWithdrawalOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для создания операции снятия наличных денег.

        :param request: Словарь с данными для создания операции.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-cash-withdrawal-operation", json=request)

    def get_operation(self, operation_id: str) -> GetOperationResponseDict:
        """
        Получить информацию об операции по её идентификатору.

        :param operation_id: Уникальный идентификатор операции.
        :return: Словарь с данными об операции.
        """
        response = self.get_operation_api(operation_id)
        return response.json()

    def get_operation_receipt(self, operation_id: str) -> GetOperationReceiptResponseDict:
        """
        Получить чек по заданной операции.

        :param operation_id: Уникальный идентификатор операции.
        :return: Словарь с чеком по операции.
        """
        response = self.get_operation_receipt_api(operation_id)
        return response.json()

    def get_operations(self, account_id: str) -> GetOperationsResponseDict:
        """
        Получить список операций по счёту.

        :param account_id: Идентификатор счета.
        :return: Словарь со списком операций.
        """
        query = GetOperationsQueryDict(accountId=account_id)
        response = self.get_operations_api(query)
        return response.json()

    def get_operations_summary(self, account_id: str) -> GetOperationsSummaryResponseDict:
        """
        Получить сводную статистику операций по счёту.

        :param account_id: Идентификатор счета.
        :return: Словарь со статистикой операций.
        """
        query = GetOperationsSummaryQueryDict(accountId=account_id)
        response = self.get_operations_summary_api(query)
        return response.json()

    def make_fee_operation(self, card_id: str, account_id: str) -> MakeFeeOperationResponseDict:
        """
        Создать операцию комиссии.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счета.
        :return: Словарь с результатом операции.
        """
        request = MakeFeeOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_fee_operation_api(request)
        return response.json()

    def make_top_up_operation(self, card_id: str, account_id: str) -> MakeTopUpOperationResponseDict:
        """
        Создать операцию пополнения счёта.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счета.
        :return: Словарь с результатом операции.
        """
        request = MakeTopUpOperationRequestDict(
            status="COMPLETED",
            amount=1500.11,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_top_up_operation_api(request)
        return response.json()

    def make_cashback_operation(self, card_id: str, account_id: str) -> MakeCashbackOperationResponseDict:
        """
        Создать операцию начисления кэшбэка.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счета.
        :return: Словарь с результатом операции.
        """
        request = MakeCashbackOperationRequestDict(
            status="COMPLETED",
            amount=100.0,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_cashback_operation_api(request)
        return response.json()

    def make_transfer_operation(self, card_id: str, account_id: str) -> MakeTransferOperationResponseDict:
        """
        Создать операцию перевода средств.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счета.
        :return: Словарь с результатом операции.
        """
        request = MakeTransferOperationRequestDict(
            status="COMPLETED",
            amount=500.0,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_transfer_operation_api(request)
        return response.json()

    def make_purchase_operation(self, card_id: str, account_id: str,
                                category: str = "supermarkets") -> MakePurchaseOperationResponseDict:
        """
        Создать операцию покупки.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счета.
        :param category: Категория покупки.
        :return: Словарь с результатом операции.
        """
        request = MakePurchaseOperationRequestDict(
            status="COMPLETED",
            amount=300.50,
            cardId=card_id,
            accountId=account_id,
            category=category
        )
        response = self.make_purchase_operation_api(request)
        return response.json()

    def make_bill_payment_operation(self, card_id: str, account_id: str) -> MakeBillPaymentOperationResponseDict:
        """
        Создать операцию оплаты счёта.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счета.
        :return: Словарь с результатом операции.
        """
        request = MakeBillPaymentOperationRequestDict(
            status="COMPLETED",
            amount=120.0,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_bill_payment_operation_api(request)
        return response.json()

    def make_cash_withdrawal_operation(self, card_id: str, account_id: str) -> MakeCashWithdrawalOperationResponseDict:
        """
        Создать операцию снятия наличных средств.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счета.
        :return: Словарь с результатом операции.
        """
        request = MakeCashWithdrawalOperationRequestDict(
            status="COMPLETED",
            amount=1000.0,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_cash_withdrawal_operation_api(request)
        return response.json()


def build_operations_gateway_http_client() -> OperationsGatewayHTTPClient:
    """
    Функция создаёт экземпляр OperationsGatewayHTTPClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию OperationsGatewayHTTPClient.
    """
    return OperationsGatewayHTTPClient(client=build_gateway_http_client())
