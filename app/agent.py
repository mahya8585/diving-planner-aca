


def agent_general(request_message: str):
    """
    汎用エージェント。素のAOAIで回答を生成する。
    :param request_message: 入力メッセージ
    :return: response_message: 応答メッセージ
    """

    # TODO 汎用エージェントの実装


    return ''


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
    api_names = operate(request_message)

    # エージェントが見つからなかった場合は汎用エージェントを使って返答を作成する
    if len(api_names) == 0:
        return 'すみません、その質問にはお答えできません'

    return ''