import logging
import json

import azure.functions as func

def main(myblob: func.InputStream, context: func.Context):
    _d = myblob.read().decode("utf-8")
    logging.info(f"Python blob trigger function processed blob "
                 f"Name: {myblob.name}")
    _d = json.loads(_d)
    logging.info(f"BLOB DATA:\n {json.dumps(_d)}")
    logging.info(
        json.dumps({
        'ctx_func_name': context.function_name,
        'ctx_func_dir': context.function_directory,
        'ctx_invocation_id': context.invocation_id,
        'ctx_trace_context_Traceparent': context.trace_context.Traceparent,
        'ctx_trace_context_Tracestate': context.trace_context.Tracestate,
        'ctx_retry_context_RetryCount': context.retry_context.retry_count,
        'ctx_retry_context_MaxRetryCount': context.retry_context.max_retry_count,
    })
    )


