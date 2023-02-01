import typing_extensions

from openapi_client.apis.tags import TagValues
from openapi_client.apis.tags.account_api import AccountApi
from openapi_client.apis.tags.application_api import ApplicationApi
from openapi_client.apis.tags.backup_api import BackupApi
from openapi_client.apis.tags.baremetal_api import BaremetalApi
from openapi_client.apis.tags.billing_api import BillingApi
from openapi_client.apis.tags.block_api import BlockApi
from openapi_client.apis.tags.dns_api import DnsApi
from openapi_client.apis.tags.firewall_api import FirewallApi
from openapi_client.apis.tags.instances_api import InstancesApi
from openapi_client.apis.tags.iso_api import IsoApi
from openapi_client.apis.tags.kubernetes_api import KubernetesApi
from openapi_client.apis.tags.load_balancer_api import LoadBalancerApi
from openapi_client.apis.tags.s3_api import S3Api
from openapi_client.apis.tags.os_api import OsApi
from openapi_client.apis.tags.plans_api import PlansApi
from openapi_client.apis.tags.private_networks_api import PrivateNetworksApi
from openapi_client.apis.tags.vpcs_api import VPCsApi
from openapi_client.apis.tags.reserved_ip_api import ReservedIpApi
from openapi_client.apis.tags.region_api import RegionApi
from openapi_client.apis.tags.snapshot_api import SnapshotApi
from openapi_client.apis.tags.ssh_api import SshApi
from openapi_client.apis.tags.startup_api import StartupApi
from openapi_client.apis.tags.users_api import UsersApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.ACCOUNT: AccountApi,
        TagValues.APPLICATION: ApplicationApi,
        TagValues.BACKUP: BackupApi,
        TagValues.BAREMETAL: BaremetalApi,
        TagValues.BILLING: BillingApi,
        TagValues.BLOCK: BlockApi,
        TagValues.DNS: DnsApi,
        TagValues.FIREWALL: FirewallApi,
        TagValues.INSTANCES: InstancesApi,
        TagValues.ISO: IsoApi,
        TagValues.KUBERNETES: KubernetesApi,
        TagValues.LOADBALANCER: LoadBalancerApi,
        TagValues.S3: S3Api,
        TagValues.OS: OsApi,
        TagValues.PLANS: PlansApi,
        TagValues.PRIVATE_NETWORKS: PrivateNetworksApi,
        TagValues.VPCS: VPCsApi,
        TagValues.RESERVEDIP: ReservedIpApi,
        TagValues.REGION: RegionApi,
        TagValues.SNAPSHOT: SnapshotApi,
        TagValues.SSH: SshApi,
        TagValues.STARTUP: StartupApi,
        TagValues.USERS: UsersApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.ACCOUNT: AccountApi,
        TagValues.APPLICATION: ApplicationApi,
        TagValues.BACKUP: BackupApi,
        TagValues.BAREMETAL: BaremetalApi,
        TagValues.BILLING: BillingApi,
        TagValues.BLOCK: BlockApi,
        TagValues.DNS: DnsApi,
        TagValues.FIREWALL: FirewallApi,
        TagValues.INSTANCES: InstancesApi,
        TagValues.ISO: IsoApi,
        TagValues.KUBERNETES: KubernetesApi,
        TagValues.LOADBALANCER: LoadBalancerApi,
        TagValues.S3: S3Api,
        TagValues.OS: OsApi,
        TagValues.PLANS: PlansApi,
        TagValues.PRIVATE_NETWORKS: PrivateNetworksApi,
        TagValues.VPCS: VPCsApi,
        TagValues.RESERVEDIP: ReservedIpApi,
        TagValues.REGION: RegionApi,
        TagValues.SNAPSHOT: SnapshotApi,
        TagValues.SSH: SshApi,
        TagValues.STARTUP: StartupApi,
        TagValues.USERS: UsersApi,
    }
)
