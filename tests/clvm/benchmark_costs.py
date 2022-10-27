from floteo.types.blockchain_format.program import INFINITE_COST
from floteo.types.spend_bundle import SpendBundle
from floteo.types.generator_types import BlockGenerator
from floteo.consensus.cost_calculator import NPCResult
from floteo.consensus.default_constants import DEFAULT_CONSTANTS
from floteo.full_node.bundle_tools import simple_solution_generator
from floteo.full_node.mempool_check_conditions import get_name_puzzle_conditions


def cost_of_spend_bundle(spend_bundle: SpendBundle) -> int:
    program: BlockGenerator = simple_solution_generator(spend_bundle)
    npc_result: NPCResult = get_name_puzzle_conditions(
        program, INFINITE_COST, cost_per_byte=DEFAULT_CONSTANTS.COST_PER_BYTE, mempool_mode=True
    )
    return npc_result.cost
