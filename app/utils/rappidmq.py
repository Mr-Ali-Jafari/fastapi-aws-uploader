import pika

async def rappid_mq(filename: str,file_content: bytes,rabbitmq_host:str = 'localhost',queue_name: str = 'rappid_queue'):
    # connect to rabbitmq   
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host))
    channel = connection.channel()
    channel.queue_declare(queue=queue_name)

    # send the file to rabbitmq
    channel.basic_publish(
        exchange='',
        routing_key=queue_name,
        body=file_content,
        properties=pika.BasicProperties(
            content_type='application/octet-stream',
            delivery_mode=2,
        )

        )
    print(f"file {filename} sent to rabbitmq")
    connection.close()
