import logging

import algokit_utils
from algosdk.v2client.algod import AlgodClient
from algosdk.v2client.indexer import IndexerClient

logger = logging.getLogger(__name__)


# define deployment behaviour based on supplied app spec
def deploy(
    algod_client: AlgodClient,
    indexer_client: IndexerClient,
    app_spec: algokit_utils.ApplicationSpecification,
    deployer: algokit_utils.Account,
) -> None:
    from smart_contracts.artifacts.counter.counter_client import (
        CounterClient,
    )

    app_client = CounterClient(
        algod_client,
        creator=deployer,
        indexer_client=indexer_client,
    )

    app_client.deploy(
        on_schema_break=algokit_utils.OnSchemaBreak.AppendApp,
        on_update=algokit_utils.OnUpdate.AppendApp,
    )

    globalState = app_client.app_client.get_global_state()
    logger.info(
        f"Deployed {app_spec.contract.name} ({app_client.app_id}) with global state: {globalState}"
    )

    result =app_client.increment()
    globalState = app_client.app_client.get_global_state()
    logger.info(
        f"incremented counter txid: {result.tx_id} with global state: {globalState}"
    )

    result =app_client.decrement()
    globalState = app_client.app_client.get_global_state()
    logger.info(
        f"decremented counter txid: {result.tx_id} with global state: {globalState}"
    )
