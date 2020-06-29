k = KubernetesPodOperator(namespace='airflow',
                          image="ubuntu:16.04",
                          cmds=["bash", "-cx"],
                          arguments=["echo", "10"],
                          labels={"foo": "bar"},
                          ports=["80"]
                          name="kube-test",
                          task_id="task",
                          is_delete_operator_pod=True,
                          hostnetwork=False,
                          )
