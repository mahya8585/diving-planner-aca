import requests
from concurrent.futures import ThreadPoolExecutor, as_completed


def call_agent_general(request_message: str):
    """
    汎用エージェント。素のAOAIで回答を生成する。
    :param request_message: 入力メッセージ
    :return: response_message: 応答メッセージ
    """

    # TODO 汎用エージェントの実装


    return ''

def call_agent_multi(request_message: str, agent_name: str):
    """
    各種エージェントの呼び出し。
    1 functions app内のエンドポイントを呼び分ける想定
    :param request_message: リクエストメッセージ
    :return: response_message: 応答メッセージ
    """
    response_message = requests.post(agent_name, json={"message": request_message})
    return response_message.json()


def operate(message: str):
    """
    ユーザからの入力を受け取り、どのエージェントに質問すればよいか判定する
    :param message: 入力メッセージ
    :return: api_names: API名のリスト
    """

    # TODO オペレータエージェントの呼び出し

    api_names = []
    return api_names


def response(request_message: str):
    """
    ユーザからの入力を受け取り、応答メッセージを返す
    :param request_message: 入力メッセージ
    :return: response_message: 応答メッセージ
    """

    # オペレータエージェント使って呼び出すエージェントを判定させる
    agent_names = operate(request_message)

    # エージェントが見つからなかった場合は汎用エージェントを使って返答を作成する
    if len(agent_names) == 0:
        return call_agent_general(request_message)

    # リストにあるAPIに対して並列呼び出しをおこなう
    responses = []
    with ThreadPoolExecutor():
        future_to_api = {ThreadPoolExecutor().submit(
            call_agent_multi, request_message, agent_name): agent_name for agent_name in agent_names}

        for future in as_completed(future_to_api):
            api_name = future_to_api[future]
            try:
                data = future.result()
                responses.append(data)
            except Exception as exc:
                print(f'{api_name} generated an exception: {exc}')

    # TODO: ここで土のメッセージがだれの応答メッセージなのかを明記したデータを生成する
    return responses