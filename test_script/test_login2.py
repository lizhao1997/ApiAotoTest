import pytest

from zonghe.baw import Member
from zonghe.caw import DataRead, MySqlOp
from zonghe.test_script.conftest import db_info
from zonghe.test_script.test_login import setup_data


@pytest.fixture(params=DataRead.read_yaml(r"test_data\login.yaml"))
def login_data(request):
    return request.param


def test_login(login_data, baserequest, url):
    # 初始化环境：避免环境中已有本次测试用到的数据
    MySqlOp.delete_user(db_info, setup_data['data']['mobilephone'])
    # 注册用户
    Member.register(baserequest, url, setup_data['regdata'])
    print("注册数据", login_data['regdata'])
    # 登录
    print("登录数据", login_data['logindata'])
    # 检查结果
    # 删除注册用户
