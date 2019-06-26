from eth2.beacon.state_machines.forks.serenity.configs import (
    SERENITY_CONFIG,
)


XIAO_LONG_BAO_CONFIG = SERENITY_CONFIG._replace(
    SLOTS_PER_EPOCH=4,
    TARGET_COMMITTEE_SIZE=2,
    SHARD_COUNT=4,
    MIN_ATTESTATION_INCLUSION_DELAY=2,
)
