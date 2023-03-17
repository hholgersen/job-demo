from kubernetes import client, config
import uuid

def create_kubernetes_job():

    # Load in-cluster config or kubeconfig, depending on the environment

    job_name = "job-" + str(uuid.uuid1())
    try:
        config.load_incluster_config()
    except config.ConfigException:
        config.load_kube_config()

    api_instance = client.BatchV1Api()

    job = client.V1Job(
        api_version="batch/v1",
        kind="Job",
        metadata=client.V1ObjectMeta(name=job_name),
        spec=client.V1JobSpec(
            template=client.V1PodTemplateSpec(
                metadata=client.V1ObjectMeta(labels={"app": "pylaunched"}),
                spec=client.V1PodSpec(
                    containers=[
                        client.V1Container(
                            name="job-container",
                            image="busybox",
                            command=["sh", "-c", "echo 'Hello, Kubernetes Job!' && sleep 30"]
                        )
                    ],
                    restart_policy="Never"
                )
            ),
            backoff_limit=4
        )
    )

    api_response = api_instance.create_namespaced_job(
        namespace="k8j", body=job
    )

    print("Job created: %s" % api_response.metadata.name)

if __name__ == "__main__":
    create_kubernetes_job()