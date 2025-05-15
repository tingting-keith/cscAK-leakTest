db_config = DbConfig(
    params={
        'secret_name': "test",
        'ip_address': "999.999.999.999",
        'port': 987654321,
        'db_name': "database_name",
        'param_str': "charset=utf8&loc=Local",
    })
ssm_service_config = SsmAccount(
    params={
        'secret_id': "IKIDlT7fafgeeYMDycDmKoBTzdBYjpmX6YKw",
        'secret_key': "UnaJwTy5ENSeotxw1znU0KSOHPPEwUwP",
        'url': test_url,
        'region': "ap-hongkong"
    })
config = Config(
    params={
        'db_config': db_config,
        'ssm_service_config': ssm_service_config,
        'WATCH_FREQ': 10
    })

db_conn = DynamicSecretRotationDb()
err = db_conn.init(config)

c = db_conn.get_conn()
try:
    c.ping()
except TencentCloudSDKException as e:
	logging.error("failed to access db with err: {0}".format(str(
            e.args[0])).encode("utf-8"))

c.close()
