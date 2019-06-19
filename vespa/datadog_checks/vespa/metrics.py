GAUGE = 'gauge'
PERCENTILE = 'percentile'
COUNTER = 'counter'

CONTAINER_METRICS = {
    'degraded_queries':
    ('vespa.degraded_queries', COUNTER),
    'documents_covered':
    ('vespa.documents_covered', COUNTER),
    'documents_total':
    ('vespa.documents_total', COUNTER),
    'empty_results':
    ('vespa.empty_results', COUNTER),
    'error.timeout':
    ('vespa.error.timeout', COUNTER),
    'failed_queries':
    ('vespa.failed_queries', COUNTER),
    'handled.latency':
    ('vespa.handled.latency', GAUGE),
    'handled.requests':
    ('vespa.handled.requests', COUNTER),
    'hits_per_query':
    ('vespa.hits_per_query', GAUGE),
    'http.status.1xx':
    ('vespa.http.status.1xx', COUNTER),
    'http.status.2xx':
    ('vespa.http.status.2xx', COUNTER),
    'http.status.3xx':
    ('vespa.http.status.3xx', COUNTER),
    'http.status.401':
    ('vespa.http.status.401', COUNTER),
    'http.status.403':
    ('vespa.http.status.403', COUNTER),
    'http.status.4xx':
    ('vespa.http.status.4xx', COUNTER),
    'http.status.5xx':
    ('vespa.http.status.5xx', COUNTER),
    'jdisc.deactivated_containers.total':
    ('vespa.jdisc.deactivated_containers.total', GAUGE),
    'jdisc.gc.count':
    ('vespa.jdisc.gc.count', GAUGE),
    'jdisc.gc.ms':
    ('vespa.jdisc.gc.ms', GAUGE),
    'jdisc.http.request.content_size':
    ('vespa.jdisc.http.request.content_size', GAUGE),
    'jdisc.http.request.prematurely_closed':
    ('vespa.jdisc.http.request.prematurely_closed', COUNTER),
    'jdisc.http.request.uri_length':
    ('vespa.jdisc.http.request.uri_length', GAUGE),
    'jdisc.http.requests':
    ('vespa.jdisc.http.requests', COUNTER),
    'jdisc.http.requests.status':
    ('vespa.jdisc.http.requests.status', COUNTER),
    'jdisc.memory_mappings':
    ('vespa.jdisc.memory_mappings', GAUGE),
    'jdisc.open_file_descriptors':
    ('vespa.jdisc.open_file_descriptors', GAUGE),
    'jrt.transport.client.tls-connections-established':
    ('vespa.jrt.transport.client.tls-connections-established', COUNTER),
    'jrt.transport.server.tls-connections-established':
    ('vespa.jrt.transport.server.tls-connections-established', COUNTER),
    'max_query_latency':
    ('vespa.max_query_latency', GAUGE),
    'mean_query_latency':
    ('vespa.mean_query_latency', GAUGE),
    'mem.heap.free':
    ('vespa.mem.heap.free', GAUGE),
    'mem.heap.total':
    ('vespa.mem.heap.total', GAUGE),
    'mem.heap.used':
    ('vespa.mem.heap.used', GAUGE),
    'peak_qps':
    ('vespa.peak_qps', GAUGE),
    'queries':
    ('vespa.queries', COUNTER),
    'query_container_latency':
    ('vespa.query_container_latency', GAUGE),
    'query_latency':
    ('vespa.query_latency', GAUGE),
    'relevance.at_1':
    ('vespa.relevance.at_1', GAUGE),
    'relevance.at_10':
    ('vespa.relevance.at_10', GAUGE),
    'relevance.at_3':
    ('vespa.relevance.at_3', GAUGE),
    'search_connections':
    ('vespa.search_connections', GAUGE),
    'serverActiveThreads':
    ('vespa.serverActiveThreads', GAUGE),
    'serverBytesSent':
    ('vespa.serverBytesSent', GAUGE),
    'serverConnectionDurationMax':
    ('vespa.serverConnectionDurationMax', GAUGE),
    'serverConnectionDurationMean':
    ('vespa.serverConnectionDurationMean', GAUGE),
    'serverConnectionDurationStdDev':
    ('vespa.serverConnectionDurationStdDev', GAUGE),
    'serverConnectionsOpenMax':
    ('vespa.serverConnectionsOpenMax', GAUGE),
    'serverNumConnections':
    ('vespa.serverNumConnections', GAUGE),
    'serverNumFailedResponses':
    ('vespa.serverNumFailedResponses', COUNTER),
    'serverNumOpenConnections':
    ('vespa.serverNumOpenConnections', GAUGE),
    'serverNumRequests':
    ('vespa.serverNumRequests', COUNTER),
    'serverNumSuccessfulResponseWrites':
    ('vespa.serverNumSuccessfulResponseWrites', COUNTER),
    'serverNumSuccessfulResponses':
    ('vespa.serverNumSuccessfulResponses', COUNTER),
    'serverStartedMillis':
    ('vespa.serverStartedMillis', GAUGE),
    'serverThreadPoolSize':
    ('vespa.serverThreadPoolSize', GAUGE),
    'serverTimeToFirstByte':
    ('vespa.serverTimeToFirstByte', GAUGE),
    'serverTotalFailedResponseLatency':
    ('vespa.serverTotalFailedResponseLatency', GAUGE),
    'serverTotalSuccessfulResponseLatency':
    ('vespa.serverTotalSuccessfulResponseLatency', GAUGE),
    'totalhits_per_query':
    ('vespa.totalhits_per_query', GAUGE),
}

CONTENT_METRICS = {
    'content.proton.docsum.count':
    ('vespa.content.proton.docsum.count', COUNTER),
    'content.proton.docsum.docs':
    ('vespa.content.proton.docsum.docs', COUNTER),
    'content.proton.docsum.latency':
    ('vespa.content.proton.docsum.latency', GAUGE),
    'content.proton.documentdb.attribute.memory_usage.allocated_bytes':
    ('vespa.content.proton.documentdb.attribute.memory_usage.allocated_bytes', GAUGE),
    'content.proton.documentdb.attribute.memory_usage.dead_bytes':
    ('vespa.content.proton.documentdb.attribute.memory_usage.dead_bytes', GAUGE),
    'content.proton.documentdb.attribute.memory_usage.onhold_bytes':
    ('vespa.content.proton.documentdb.attribute.memory_usage.onhold_bytes', GAUGE),
    'content.proton.documentdb.attribute.memory_usage.used_bytes':
    ('vespa.content.proton.documentdb.attribute.memory_usage.used_bytes', GAUGE),
    'content.proton.documentdb.attribute.resource_usage.enum_store':
    ('vespa.content.proton.documentdb.attribute.resource_usage.enum_store', GAUGE),
    'content.proton.documentdb.attribute.resource_usage.feeding_blocked':
    ('vespa.content.proton.documentdb.attribute.resource_usage.feeding_blocked', GAUGE),
    'content.proton.documentdb.attribute.resource_usage.multi_value':
    ('vespa.content.proton.documentdb.attribute.resource_usage.multi_value', GAUGE),
    'content.proton.documentdb.disk_usage':
    ('vespa.content.proton.documentdb.disk_usage', GAUGE),
    'content.proton.documentdb.documents.active':
    ('vespa.content.proton.documentdb.documents.active', GAUGE),
    'content.proton.documentdb.documents.ready':
    ('vespa.content.proton.documentdb.documents.ready', GAUGE),
    'content.proton.documentdb.documents.removed':
    ('vespa.content.proton.documentdb.documents.removed', GAUGE),
    'content.proton.documentdb.documents.total':
    ('vespa.content.proton.documentdb.documents.total', GAUGE),
    'content.proton.documentdb.index.disk_usage':
    ('vespa.content.proton.documentdb.index.disk_usage', GAUGE),
    'content.proton.documentdb.index.docs_in_memory':
    ('vespa.content.proton.documentdb.index.docs_in_memory', GAUGE),
    'content.proton.documentdb.index.memory_usage.allocated_bytes':
    ('vespa.content.proton.documentdb.index.memory_usage.allocated_bytes', GAUGE),
    'content.proton.documentdb.index.memory_usage.dead_bytes':
    ('vespa.content.proton.documentdb.index.memory_usage.dead_bytes', GAUGE),
    'content.proton.documentdb.index.memory_usage.onhold_bytes':
    ('vespa.content.proton.documentdb.index.memory_usage.onhold_bytes', GAUGE),
    'content.proton.documentdb.index.memory_usage.used_bytes':
    ('vespa.content.proton.documentdb.index.memory_usage.used_bytes', GAUGE),
    'content.proton.documentdb.job.attribute_flush':
    ('vespa.content.proton.documentdb.job.attribute_flush', GAUGE),
    'content.proton.documentdb.job.bucket_move':
    ('vespa.content.proton.documentdb.job.bucket_move', GAUGE),
    'content.proton.documentdb.job.disk_index_fusion':
    ('vespa.content.proton.documentdb.job.disk_index_fusion', GAUGE),
    'content.proton.documentdb.job.document_store_compact':
    ('vespa.content.proton.documentdb.job.document_store_compact', GAUGE),
    'content.proton.documentdb.job.document_store_flush':
    ('vespa.content.proton.documentdb.job.document_store_flush', GAUGE),
    'content.proton.documentdb.job.lid_space_compact':
    ('vespa.content.proton.documentdb.job.lid_space_compact', GAUGE),
    'content.proton.documentdb.job.memory_index_flush':
    ('vespa.content.proton.documentdb.job.memory_index_flush', GAUGE),
    'content.proton.documentdb.job.removed_documents_prune':
    ('vespa.content.proton.documentdb.job.removed_documents_prune', GAUGE),
    'content.proton.documentdb.job.total':
    ('vespa.content.proton.documentdb.job.total', GAUGE),
    'content.proton.documentdb.matching.docs_matched':
    ('vespa.content.proton.documentdb.matching.docs_matched', COUNTER),
    'content.proton.documentdb.matching.docs_ranked':
    ('vespa.content.proton.documentdb.matching.docs_ranked', COUNTER),
    'content.proton.documentdb.matching.docs_reranked':
    ('vespa.content.proton.documentdb.matching.docs_reranked', COUNTER),
    'content.proton.documentdb.matching.queries':
    ('vespa.content.proton.documentdb.matching.queries', COUNTER),
    'content.proton.documentdb.matching.query_collateral_time':
    ('vespa.content.proton.documentdb.matching.query_collateral_time', GAUGE),
    'content.proton.documentdb.matching.query_latency':
    ('vespa.content.proton.documentdb.matching.query_latency', GAUGE),
    'content.proton.documentdb.matching.rank_profile.docid_partition.active_time':
    ('vespa.content.proton.documentdb.matching.rank_profile.docid_partition.active_time', GAUGE),
    'content.proton.documentdb.matching.rank_profile.docid_partition.docs_matched':
    ('vespa.content.proton.documentdb.matching.rank_profile.docid_partition.docs_matched', COUNTER),
    'content.proton.documentdb.matching.rank_profile.docid_partition.docs_ranked':
    ('vespa.content.proton.documentdb.matching.rank_profile.docid_partition.docs_ranked', COUNTER),
    'content.proton.documentdb.matching.rank_profile.docid_partition.docs_reranked':
    ('vespa.content.proton.documentdb.matching.rank_profile.docid_partition.docs_reranked', COUNTER),
    'content.proton.documentdb.matching.rank_profile.docid_partition.wait_time':
    ('vespa.content.proton.documentdb.matching.rank_profile.docid_partition.wait_time', GAUGE),
    'content.proton.documentdb.matching.rank_profile.docs_matched':
    ('vespa.content.proton.documentdb.matching.rank_profile.docs_matched', COUNTER),
    'content.proton.documentdb.matching.rank_profile.docs_ranked':
    ('vespa.content.proton.documentdb.matching.rank_profile.docs_ranked', COUNTER),
    'content.proton.documentdb.matching.rank_profile.docs_reranked':
    ('vespa.content.proton.documentdb.matching.rank_profile.docs_reranked', COUNTER),
    'content.proton.documentdb.matching.rank_profile.grouping_time':
    ('vespa.content.proton.documentdb.matching.rank_profile.grouping_time', GAUGE),
    'content.proton.documentdb.matching.rank_profile.limited_queries':
    ('vespa.content.proton.documentdb.matching.rank_profile.limited_queries', COUNTER),
    'content.proton.documentdb.matching.rank_profile.match_time':
    ('vespa.content.proton.documentdb.matching.rank_profile.match_time', GAUGE),
    'content.proton.documentdb.matching.rank_profile.queries':
    ('vespa.content.proton.documentdb.matching.rank_profile.queries', COUNTER),
    'content.proton.documentdb.matching.rank_profile.query_collateral_time':
    ('vespa.content.proton.documentdb.matching.rank_profile.query_collateral_time', GAUGE),
    'content.proton.documentdb.matching.rank_profile.query_latency':
    ('vespa.content.proton.documentdb.matching.rank_profile.query_latency', GAUGE),
    'content.proton.documentdb.matching.rank_profile.rerank_time':
    ('vespa.content.proton.documentdb.matching.rank_profile.rerank_time', GAUGE),
    'content.proton.documentdb.matching.rank_profile.soft_doomed_queries':
    ('vespa.content.proton.documentdb.matching.rank_profile.soft_doomed_queries', COUNTER),
    'content.proton.documentdb.matching.soft_doom_factor':
    ('vespa.content.proton.documentdb.matching.soft_doom_factor', GAUGE),
    'content.proton.documentdb.matching.soft_doomed_queries':
    ('vespa.content.proton.documentdb.matching.soft_doomed_queries', COUNTER),
    'content.proton.documentdb.memory_usage.allocated_bytes':
    ('vespa.content.proton.documentdb.memory_usage.allocated_bytes', GAUGE),
    'content.proton.documentdb.memory_usage.dead_bytes':
    ('vespa.content.proton.documentdb.memory_usage.dead_bytes', GAUGE),
    'content.proton.documentdb.memory_usage.onhold_bytes':
    ('vespa.content.proton.documentdb.memory_usage.onhold_bytes', GAUGE),
    'content.proton.documentdb.memory_usage.used_bytes':
    ('vespa.content.proton.documentdb.memory_usage.used_bytes', GAUGE),
    'content.proton.documentdb.notready.attribute.memory_usage.allocated_bytes':
    ('vespa.content.proton.documentdb.notready.attribute.memory_usage.allocated_bytes', GAUGE),
    'content.proton.documentdb.notready.attribute.memory_usage.dead_bytes':
    ('vespa.content.proton.documentdb.notready.attribute.memory_usage.dead_bytes', GAUGE),
    'content.proton.documentdb.notready.attribute.memory_usage.onhold_bytes':
    ('vespa.content.proton.documentdb.notready.attribute.memory_usage.onhold_bytes', GAUGE),
    'content.proton.documentdb.notready.attribute.memory_usage.used_bytes':
    ('vespa.content.proton.documentdb.notready.attribute.memory_usage.used_bytes', GAUGE),
    'content.proton.documentdb.notready.document_store.cache.elements':
    ('vespa.content.proton.documentdb.notready.document_store.cache.elements', GAUGE),
    'content.proton.documentdb.notready.document_store.cache.hit_rate':
    ('vespa.content.proton.documentdb.notready.document_store.cache.hit_rate', GAUGE),
    'content.proton.documentdb.notready.document_store.cache.invalidations':
    ('vespa.content.proton.documentdb.notready.document_store.cache.invalidations', COUNTER),
    'content.proton.documentdb.notready.document_store.cache.lookups':
    ('vespa.content.proton.documentdb.notready.document_store.cache.lookups', COUNTER),
    'content.proton.documentdb.notready.document_store.cache.memory_usage':
    ('vespa.content.proton.documentdb.notready.document_store.cache.memory_usage', GAUGE),
    'content.proton.documentdb.notready.document_store.disk_bloat':
    ('vespa.content.proton.documentdb.notready.document_store.disk_bloat', GAUGE),
    'content.proton.documentdb.notready.document_store.disk_usage':
    ('vespa.content.proton.documentdb.notready.document_store.disk_usage', GAUGE),
    'content.proton.documentdb.notready.document_store.max_bucket_spread':
    ('vespa.content.proton.documentdb.notready.document_store.max_bucket_spread', GAUGE),
    'content.proton.documentdb.notready.document_store.memory_usage.allocated_bytes':
    ('vespa.content.proton.documentdb.notready.document_store.memory_usage.allocated_bytes', GAUGE),
    'content.proton.documentdb.notready.document_store.memory_usage.dead_bytes':
    ('vespa.content.proton.documentdb.notready.document_store.memory_usage.dead_bytes', GAUGE),
    'content.proton.documentdb.notready.document_store.memory_usage.onhold_bytes':
    ('vespa.content.proton.documentdb.notready.document_store.memory_usage.onhold_bytes', GAUGE),
    'content.proton.documentdb.notready.document_store.memory_usage.used_bytes':
    ('vespa.content.proton.documentdb.notready.document_store.memory_usage.used_bytes', GAUGE),
    'content.proton.documentdb.notready.lid_space.highest_used_lid':
    ('vespa.content.proton.documentdb.notready.lid_space.highest_used_lid', GAUGE),
    'content.proton.documentdb.notready.lid_space.lid_bloat_factor':
    ('vespa.content.proton.documentdb.notready.lid_space.lid_bloat_factor', GAUGE),
    'content.proton.documentdb.notready.lid_space.lid_fragmentation_factor':
    ('vespa.content.proton.documentdb.notready.lid_space.lid_fragmentation_factor', GAUGE),
    'content.proton.documentdb.notready.lid_space.lid_limit':
    ('vespa.content.proton.documentdb.notready.lid_space.lid_limit', GAUGE),
    'content.proton.documentdb.notready.lid_space.lowest_free_lid':
    ('vespa.content.proton.documentdb.notready.lid_space.lowest_free_lid', GAUGE),
    'content.proton.documentdb.notready.lid_space.used_lids':
    ('vespa.content.proton.documentdb.notready.lid_space.used_lids', GAUGE),
    'content.proton.documentdb.ready.attribute.memory_usage.allocated_bytes':
    ('vespa.content.proton.documentdb.ready.attribute.memory_usage.allocated_bytes', GAUGE),
    'content.proton.documentdb.ready.attribute.memory_usage.dead_bytes':
    ('vespa.content.proton.documentdb.ready.attribute.memory_usage.dead_bytes', GAUGE),
    'content.proton.documentdb.ready.attribute.memory_usage.onhold_bytes':
    ('vespa.content.proton.documentdb.ready.attribute.memory_usage.onhold_bytes', GAUGE),
    'content.proton.documentdb.ready.attribute.memory_usage.used_bytes':
    ('vespa.content.proton.documentdb.ready.attribute.memory_usage.used_bytes', GAUGE),
    'content.proton.documentdb.ready.document_store.cache.elements':
    ('vespa.content.proton.documentdb.ready.document_store.cache.elements', GAUGE),
    'content.proton.documentdb.ready.document_store.cache.hit_rate':
    ('vespa.content.proton.documentdb.ready.document_store.cache.hit_rate', GAUGE),
    'content.proton.documentdb.ready.document_store.cache.invalidations':
    ('vespa.content.proton.documentdb.ready.document_store.cache.invalidations', COUNTER),
    'content.proton.documentdb.ready.document_store.cache.lookups':
    ('vespa.content.proton.documentdb.ready.document_store.cache.lookups', COUNTER),
    'content.proton.documentdb.ready.document_store.cache.memory_usage':
    ('vespa.content.proton.documentdb.ready.document_store.cache.memory_usage', GAUGE),
    'content.proton.documentdb.ready.document_store.disk_bloat':
    ('vespa.content.proton.documentdb.ready.document_store.disk_bloat', GAUGE),
    'content.proton.documentdb.ready.document_store.disk_usage':
    ('vespa.content.proton.documentdb.ready.document_store.disk_usage', GAUGE),
    'content.proton.documentdb.ready.document_store.max_bucket_spread':
    ('vespa.content.proton.documentdb.ready.document_store.max_bucket_spread', GAUGE),
    'content.proton.documentdb.ready.document_store.memory_usage.allocated_bytes':
    ('vespa.content.proton.documentdb.ready.document_store.memory_usage.allocated_bytes', GAUGE),
    'content.proton.documentdb.ready.document_store.memory_usage.dead_bytes':
    ('vespa.content.proton.documentdb.ready.document_store.memory_usage.dead_bytes', GAUGE),
    'content.proton.documentdb.ready.document_store.memory_usage.onhold_bytes':
    ('vespa.content.proton.documentdb.ready.document_store.memory_usage.onhold_bytes', GAUGE),
    'content.proton.documentdb.ready.document_store.memory_usage.used_bytes':
    ('vespa.content.proton.documentdb.ready.document_store.memory_usage.used_bytes', GAUGE),
    'content.proton.documentdb.ready.lid_space.highest_used_lid':
    ('vespa.content.proton.documentdb.ready.lid_space.highest_used_lid', GAUGE),
    'content.proton.documentdb.ready.lid_space.lid_bloat_factor':
    ('vespa.content.proton.documentdb.ready.lid_space.lid_bloat_factor', GAUGE),
    'content.proton.documentdb.ready.lid_space.lid_fragmentation_factor':
    ('vespa.content.proton.documentdb.ready.lid_space.lid_fragmentation_factor', GAUGE),
    'content.proton.documentdb.ready.lid_space.lid_limit':
    ('vespa.content.proton.documentdb.ready.lid_space.lid_limit', GAUGE),
    'content.proton.documentdb.ready.lid_space.lowest_free_lid':
    ('vespa.content.proton.documentdb.ready.lid_space.lowest_free_lid', GAUGE),
    'content.proton.documentdb.ready.lid_space.used_lids':
    ('vespa.content.proton.documentdb.ready.lid_space.used_lids', GAUGE),
    'content.proton.documentdb.removed.document_store.cache.elements':
    ('vespa.content.proton.documentdb.removed.document_store.cache.elements', GAUGE),
    'content.proton.documentdb.removed.document_store.cache.hit_rate':
    ('vespa.content.proton.documentdb.removed.document_store.cache.hit_rate', GAUGE),
    'content.proton.documentdb.removed.document_store.cache.invalidations':
    ('vespa.content.proton.documentdb.removed.document_store.cache.invalidations', COUNTER),
    'content.proton.documentdb.removed.document_store.cache.lookups':
    ('vespa.content.proton.documentdb.removed.document_store.cache.lookups', COUNTER),
    'content.proton.documentdb.removed.document_store.cache.memory_usage':
    ('vespa.content.proton.documentdb.removed.document_store.cache.memory_usage', GAUGE),
    'content.proton.documentdb.removed.document_store.disk_bloat':
    ('vespa.content.proton.documentdb.removed.document_store.disk_bloat', GAUGE),
    'content.proton.documentdb.removed.document_store.disk_usage':
    ('vespa.content.proton.documentdb.removed.document_store.disk_usage', GAUGE),
    'content.proton.documentdb.removed.document_store.max_bucket_spread':
    ('vespa.content.proton.documentdb.removed.document_store.max_bucket_spread', GAUGE),
    'content.proton.documentdb.removed.document_store.memory_usage.allocated_bytes':
    ('vespa.content.proton.documentdb.removed.document_store.memory_usage.allocated_bytes', GAUGE),
    'content.proton.documentdb.removed.document_store.memory_usage.dead_bytes':
    ('vespa.content.proton.documentdb.removed.document_store.memory_usage.dead_bytes', GAUGE),
    'content.proton.documentdb.removed.document_store.memory_usage.onhold_bytes':
    ('vespa.content.proton.documentdb.removed.document_store.memory_usage.onhold_bytes', GAUGE),
    'content.proton.documentdb.removed.document_store.memory_usage.used_bytes':
    ('vespa.content.proton.documentdb.removed.document_store.memory_usage.used_bytes', GAUGE),
    'content.proton.documentdb.removed.lid_space.highest_used_lid':
    ('vespa.content.proton.documentdb.removed.lid_space.highest_used_lid', GAUGE),
    'content.proton.documentdb.removed.lid_space.lid_bloat_factor':
    ('vespa.content.proton.documentdb.removed.lid_space.lid_bloat_factor', GAUGE),
    'content.proton.documentdb.removed.lid_space.lid_fragmentation_factor':
    ('vespa.content.proton.documentdb.removed.lid_space.lid_fragmentation_factor', GAUGE),
    'content.proton.documentdb.removed.lid_space.lid_limit':
    ('vespa.content.proton.documentdb.removed.lid_space.lid_limit', GAUGE),
    'content.proton.documentdb.removed.lid_space.lowest_free_lid':
    ('vespa.content.proton.documentdb.removed.lid_space.lowest_free_lid', GAUGE),
    'content.proton.documentdb.removed.lid_space.used_lids':
    ('vespa.content.proton.documentdb.removed.lid_space.used_lids', GAUGE),
    'content.proton.documentdb.session_cache.grouping.num_cached':
    ('vespa.content.proton.documentdb.session_cache.grouping.num_cached', GAUGE),
    'content.proton.documentdb.session_cache.grouping.num_dropped':
    ('vespa.content.proton.documentdb.session_cache.grouping.num_dropped', COUNTER),
    'content.proton.documentdb.session_cache.grouping.num_insert':
    ('vespa.content.proton.documentdb.session_cache.grouping.num_insert', COUNTER),
    'content.proton.documentdb.session_cache.grouping.num_pick':
    ('vespa.content.proton.documentdb.session_cache.grouping.num_pick', COUNTER),
    'content.proton.documentdb.session_cache.grouping.num_timedout':
    ('vespa.content.proton.documentdb.session_cache.grouping.num_timedout', COUNTER),
    'content.proton.documentdb.session_cache.search.num_cached':
    ('vespa.content.proton.documentdb.session_cache.search.num_cached', GAUGE),
    'content.proton.documentdb.session_cache.search.num_dropped':
    ('vespa.content.proton.documentdb.session_cache.search.num_dropped', COUNTER),
    'content.proton.documentdb.session_cache.search.num_insert':
    ('vespa.content.proton.documentdb.session_cache.search.num_insert', COUNTER),
    'content.proton.documentdb.session_cache.search.num_pick':
    ('vespa.content.proton.documentdb.session_cache.search.num_pick', COUNTER),
    'content.proton.documentdb.session_cache.search.num_timedout':
    ('vespa.content.proton.documentdb.session_cache.search.num_timedout', COUNTER),
    'content.proton.documentdb.threading_service.attribute_field_writer.accepted':
    ('vespa.content.proton.documentdb.threading_service.attribute_field_writer.accepted', COUNTER),
    'content.proton.documentdb.threading_service.attribute_field_writer.maxpending':
    ('vespa.content.proton.documentdb.threading_service.attribute_field_writer.maxpending', GAUGE),
    'content.proton.documentdb.threading_service.attribute_field_writer.rejected':
    ('vespa.content.proton.documentdb.threading_service.attribute_field_writer.rejected', COUNTER),
    'content.proton.documentdb.threading_service.index.accepted':
    ('vespa.content.proton.documentdb.threading_service.index.accepted', COUNTER),
    'content.proton.documentdb.threading_service.index.maxpending':
    ('vespa.content.proton.documentdb.threading_service.index.maxpending', GAUGE),
    'content.proton.documentdb.threading_service.index.rejected':
    ('vespa.content.proton.documentdb.threading_service.index.rejected', COUNTER),
    'content.proton.documentdb.threading_service.index_field_inverter.accepted':
    ('vespa.content.proton.documentdb.threading_service.index_field_inverter.accepted', COUNTER),
    'content.proton.documentdb.threading_service.index_field_inverter.maxpending':
    ('vespa.content.proton.documentdb.threading_service.index_field_inverter.maxpending', GAUGE),
    'content.proton.documentdb.threading_service.index_field_inverter.rejected':
    ('vespa.content.proton.documentdb.threading_service.index_field_inverter.rejected', COUNTER),
    'content.proton.documentdb.threading_service.index_field_writer.accepted':
    ('vespa.content.proton.documentdb.threading_service.index_field_writer.accepted', COUNTER),
    'content.proton.documentdb.threading_service.index_field_writer.maxpending':
    ('vespa.content.proton.documentdb.threading_service.index_field_writer.maxpending', GAUGE),
    'content.proton.documentdb.threading_service.index_field_writer.rejected':
    ('vespa.content.proton.documentdb.threading_service.index_field_writer.rejected', COUNTER),
    'content.proton.documentdb.threading_service.master.accepted':
    ('vespa.content.proton.documentdb.threading_service.master.accepted', COUNTER),
    'content.proton.documentdb.threading_service.master.maxpending':
    ('vespa.content.proton.documentdb.threading_service.master.maxpending', GAUGE),
    'content.proton.documentdb.threading_service.master.rejected':
    ('vespa.content.proton.documentdb.threading_service.master.rejected', COUNTER),
    'content.proton.documentdb.threading_service.summary.accepted':
    ('vespa.content.proton.documentdb.threading_service.summary.accepted', COUNTER),
    'content.proton.documentdb.threading_service.summary.maxpending':
    ('vespa.content.proton.documentdb.threading_service.summary.maxpending', GAUGE),
    'content.proton.documentdb.threading_service.summary.rejected':
    ('vespa.content.proton.documentdb.threading_service.summary.rejected', COUNTER),
    'content.proton.executor.docsum.accepted':
    ('vespa.content.proton.executor.docsum.accepted', COUNTER),
    'content.proton.executor.docsum.maxpending':
    ('vespa.content.proton.executor.docsum.maxpending', GAUGE),
    'content.proton.executor.docsum.rejected':
    ('vespa.content.proton.executor.docsum.rejected', COUNTER),
    'content.proton.executor.flush.accepted':
    ('vespa.content.proton.executor.flush.accepted', COUNTER),
    'content.proton.executor.flush.maxpending':
    ('vespa.content.proton.executor.flush.maxpending', GAUGE),
    'content.proton.executor.flush.rejected':
    ('vespa.content.proton.executor.flush.rejected', COUNTER),
    'content.proton.executor.match.accepted':
    ('vespa.content.proton.executor.match.accepted', COUNTER),
    'content.proton.executor.match.maxpending':
    ('vespa.content.proton.executor.match.maxpending', GAUGE),
    'content.proton.executor.match.rejected':
    ('vespa.content.proton.executor.match.rejected', COUNTER),
    'content.proton.executor.proton.accepted':
    ('vespa.content.proton.executor.proton.accepted', COUNTER),
    'content.proton.executor.proton.maxpending':
    ('vespa.content.proton.executor.proton.maxpending', GAUGE),
    'content.proton.executor.proton.rejected':
    ('vespa.content.proton.executor.proton.rejected', COUNTER),
    'content.proton.executor.shared.accepted':
    ('vespa.content.proton.executor.shared.accepted', COUNTER),
    'content.proton.executor.shared.maxpending':
    ('vespa.content.proton.executor.shared.maxpending', GAUGE),
    'content.proton.executor.shared.rejected':
    ('vespa.content.proton.executor.shared.rejected', COUNTER),
    'content.proton.executor.warmup.accepted':
    ('vespa.content.proton.executor.warmup.accepted', COUNTER),
    'content.proton.executor.warmup.maxpending':
    ('vespa.content.proton.executor.warmup.maxpending', GAUGE),
    'content.proton.executor.warmup.rejected':
    ('vespa.content.proton.executor.warmup.rejected', COUNTER),
    'content.proton.resource_usage.disk':
    ('vespa.content.proton.resource_usage.disk', GAUGE),
    'content.proton.resource_usage.disk_utilization':
    ('vespa.content.proton.resource_usage.disk_utilization', GAUGE),
    'content.proton.resource_usage.feeding_blocked':
    ('vespa.content.proton.resource_usage.feeding_blocked', GAUGE),
    'content.proton.resource_usage.memory':
    ('vespa.content.proton.resource_usage.memory', GAUGE),
    'content.proton.resource_usage.memory_mappings':
    ('vespa.content.proton.resource_usage.memory_mappings', GAUGE),
    'content.proton.resource_usage.memory_utilization':
    ('vespa.content.proton.resource_usage.memory_utilization', GAUGE),
    'content.proton.resource_usage.open_file_descriptors':
    ('vespa.content.proton.resource_usage.open_file_descriptors', GAUGE),
    'content.proton.transactionlog.disk_usage':
    ('vespa.content.proton.transactionlog.disk_usage', GAUGE),
    'content.proton.transactionlog.entries':
    ('vespa.content.proton.transactionlog.entries', GAUGE),
    'content.proton.transactionlog.replay_time':
    ('vespa.content.proton.transactionlog.replay_time', GAUGE),
    'content.proton.transport.docsum.count':
    ('vespa.content.proton.transport.docsum.count', COUNTER),
    'content.proton.transport.docsum.docs':
    ('vespa.content.proton.transport.docsum.docs', COUNTER),
    'content.proton.transport.docsum.latency':
    ('vespa.content.proton.transport.docsum.latency', GAUGE),
    'content.proton.transport.query.count':
    ('vespa.content.proton.transport.query.count', COUNTER),
    'content.proton.transport.query.latency':
    ('vespa.content.proton.transport.query.latency', GAUGE)
}


def defined_metrics():
    total = dict()
    total.update(CONTAINER_METRICS)
    total.update(CONTENT_METRICS)
    return total
