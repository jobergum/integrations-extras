GAUGE = 'gauge'
PERCENTILE = 'percentile'
COUNTER = 'counter'
RATE = 'rate'

CONTAINER_METRICS = {
    'http.status.1xx':
    ('vespa.container.http.status.1xx', RATE),
    'http.status.2xx':
    ('vespa.container.http.status.2xx', RATE),
    'http.status.3xx':
    ('vespa.container.http.status.3xx', RATE),
    'http.status.4xx':
    ('vespa.container.http.status.4xx', RATE),
    'http.status.5xx':
    ('vespa.container.http.status.5xx', RATE),
    'jdisc.gc.ms':
    ('vespa.container.gc.ms', GAUGE),
    'mem.heap.free':
    ('vespa.container.mem.heap.free', GAUGE),
    'queries':
    ('vespa.container.queries', RATE),
    'query_latency':
    ('vespa.container.query_latency', PERCENTILE),
    'hits_per_query':
    ('vespa.container.hits_per_query', GAUGE),
    'totalhits_per_query':
    ('vespa.container.totalhits_per_query', GAUGE),
    'degraded_queries':
    ('vespa.container.degraded_queries', RATE),
    'failed_queries':
    ('vespa.container.failed_queries', RATE),
    'serverActiveThreads':
    ('vespa.container.serverActiveThreads', GAUGE)
}

CONTENT_METRICS = {
    'content.proton.docsum.docs':
    ('vespa.content.proton.docsum.docs', RATE),
    'content.proton.docsum.latency':
    ('vespa.content.proton.docsum.latency', GAUGE),
    'content.proton.transport.query.count':
    ('vespa.content.proton.transport.query.count', RATE),
    'content.proton.transport.query.latency':
    ('vespa.content.proton.transport.query.latency', GAUGE),
    'content.proton.documentdb.documents.active':
    ('vespa.content.proton.documentdb.documents.active', GAUGE),
    'content.proton.documentdb.documents.ready':
    ('vespa.content.proton.documentdb.documents.ready', GAUGE),
    'content.proton.documentdb.documents.total':
    ('vespa.content.proton.documentdb.documents.total', GAUGE),
    'content.proton.documentdb.index.docs_in_memory':
    ('vespa.content.proton.documentdb.index.docs_in_memory', GAUGE),
    'content.proton.documentdb.job.total':
    ('vespa.content.proton.documentdb.job.total', GAUGE),
    'content.proton.documentdb.job.attribute_flush':
    ('vespa.content.proton.documentdb.job.attribute_flush', GAUGE),
    'content.proton.documentdb.job.disk_index_fusion':
    ('vespa.content.proton.documentdb.job.disk_index_fusion', GAUGE),
    'content.proton.documentdb.job.document_store_compact':
    ('vespa.content.proton.documentdb.job.document_store_compact', GAUGE),
    'content.proton.documentdb.job.memory_index_flush':
    ('vespa.content.proton.documentdb.job.memory_index_flush', GAUGE),
    'content.proton.documentdb.matching.docs_matched':
    ('vespa.content.proton.documentdb.matching.docs_matched', RATE),
    'content.proton.documentdb.matching.docs_reranked':
    ('vespa.content.proton.documentdb.matching.docs_reranked', RATE),
    'content.proton.documentdb.matching.rank_profile.query_latency':
    ('vespa.content.proton.documentdb.matching.rank_profile.query_latency', GAUGE),
    'content.proton.documentdb.matching.rank_profile.rerank_time':
    ('vespa.content.proton.documentdb.matching.rank_profile.rerank_time', GAUGE),
    'content.proton.documentdb.ready.document_store.cache.hit_rate':
    ('vespa.content.proton.documentdb.ready.document_store.cache.hit_rate', GAUGE),
    'content.proton.documentdb.attribute.memory_usage.allocated_bytes':
    ('vespa.content.proton.documentdb.attribute.memory_usage.allocated_bytes', GAUGE),
    'content.proton.documentdb.index.memory_usage.allocated_bytes':
    ('vespa.content.proton.documentdb.index.memory_usage.allocated_bytes', GAUGE),
    'content.proton.documentdb.disk_usage':
    ('vespa.content.proton.documentdb.disk_usage', GAUGE),
    'content.proton.documentdb.index.disk_usage':
    ('vespa.content.proton.documentdb.index.disk_usage', GAUGE),
    'content.proton.resource_usage.disk':
    ('vespa.content.proton.resource_usage.disk', GAUGE),
    'content.proton.resource_usage.disk_utilization':
    ('vespa.content.proton.resource_usage.disk_utilization', GAUGE),
    'content.proton.resource_usage.feeding_blocked':
    ('vespa.content.proton.resource_usage.feeding_blocked', GAUGE),
    'content.proton.resource_usage.memory':
    ('vespa.content.proton.resource_usage.memory', GAUGE),
    'vds.filestor.alldisks.allthreads.put.sum.count':
    ('vespa.content.put_operations', RATE),
    'vds.filestor.alldisks.allthreads.get.sum.count':
    ('vespa.content.get_operations', RATE),
    'vds.filestor.alldisks.allthreads.remove.sum.count':
    ('vespa.content.remove_operations', RATE),
    'vds.filestor.alldisks.allthreads.update.sum.count':
    ('vespa.content.update_operations', RATE),
    'vds.filestor.alldisks.allthreads.visit.sum.count':
    ('vespa.content.visit_operations', RATE)
}


def defined_metrics():
    total = dict()
    total.update(CONTAINER_METRICS)
    total.update(CONTENT_METRICS)
    return total
