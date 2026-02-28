from jmcomic import *
from jmcomic.cl import JmcomicUI

# 下方填入你要下载的本子的id，一行一个，每行的首尾可以有空白字符
jm_albums = '''

JM1271402
JM1254776
JM1258864
JM1259047
JM1251330
JM1254816
JM1255466
JM1256030
JM1257839
JM1270557
JM1066562
JM480435
JM1259128
JM1212600
JM1067641
JM652164
JM468314
JM468313
JM282250
JM217973
JM192250
JM186743
JM138812
JM138698
JM138499
JM138498
JM138494
JM136991
JM3308
JM1282268
JM1297787
JM1259045
JM1254934
JM1275917
JM1307575
JM1291802
JM1255598
JM1254592
JM1259919
JM1246982
JM1246986
JM1246983
JM1246985
JM1248542
JM1251131
JM1252453
JM1257076
JM1257279
JM1246981
JM1248539
JM1256796
JM1257075
JM1286110
JM1257188
JM1284393
JM1285975
JM1285977
JM1285976
JM1291628
JM1291747
JM1255220
JM1256084
JM1259029
JM20597
JM49529
JM61763
JM60897
JM63218
JM63084
JM62342
JM72300
JM290605
JM306810
JM139333
JM288550
JM415911
JM376555
JM376135
JM375371
JM437147
JM484293
JM572166
JM541369
JM1098388
JM1229355
JM631087
JM1167527
JM1276301
JM1255905
JM1286181
JM1256408
JM1256092
JM1276248
JM1257843
JM1256992
JM1256657
JM1257476
JM1257438
JM1304762
JM1251068
JM1256382
JM1255149
JM1256944
JM1257186
JM1257202
JM1257805
JM1270633
JM1258357
JM1259030
JM1257468
JM1297787
JM1307672
JM1275909















'''

# 单独下载章节
jm_photos = '''



'''


def env(name, default, trim=('[]', '""', "''")):
    import os
    value = os.getenv(name, None)
    if value is None or value == '':
        return default

    for pair in trim:
        if value.startswith(pair[0]) and value.endswith(pair[1]):
            value = value[1:-1]

    return value


def get_id_set(env_name, given):
    aid_set = set()
    for text in [
        given,
        (env(env_name, '')).replace('-', '\n'),
    ]:
        aid_set.update(str_to_set(text))

    return aid_set


def main():
    album_id_set = get_id_set('JM_ALBUM_IDS', jm_albums)
    photo_id_set = get_id_set('JM_PHOTO_IDS', jm_photos)

    helper = JmcomicUI()
    helper.album_id_list = list(album_id_set)
    helper.photo_id_list = list(photo_id_set)

    option = get_option()
    helper.run(option)
    option.call_all_plugin('after_download')


def get_option():
    # 读取 option 配置文件
    option = create_option(os.path.abspath(os.path.join(__file__, '../../assets/option/option_workflow_download.yml')))

    # 支持工作流覆盖配置文件的配置
    cover_option_config(option)

    # 把请求错误的html下载到文件，方便GitHub Actions下载查看日志
    log_before_raise()

    return option


def cover_option_config(option: JmOption):
    dir_rule = env('DIR_RULE', None)
    if dir_rule is not None:
        the_old = option.dir_rule
        the_new = DirRule(dir_rule, base_dir=the_old.base_dir)
        option.dir_rule = the_new

    impl = env('CLIENT_IMPL', None)
    if impl is not None:
        option.client.impl = impl

    suffix = env('IMAGE_SUFFIX', None)
    if suffix is not None:
        option.download.image.suffix = fix_suffix(suffix)

    pdf_option = env('PDF_OPTION', None)
    if pdf_option and pdf_option != '否':
        call_when = 'after_album' if pdf_option == '是 | 本子维度合并pdf' else 'after_photo'
        plugin = [{
            'plugin': Img2pdfPlugin.plugin_key,
            'kwargs': {
                'pdf_dir': option.dir_rule.base_dir + '/pdf/',
                'filename_rule': call_when[6].upper() + 'id',
                'delete_original_file': True,
            }
        }]
        option.plugins[call_when] = plugin


def log_before_raise():
    jm_download_dir = env('JM_DOWNLOAD_DIR', workspace())
    mkdir_if_not_exists(jm_download_dir)

    def decide_filepath(e):
        resp = e.context.get(ExceptionTool.CONTEXT_KEY_RESP, None)

        if resp is None:
            suffix = str(time_stamp())
        else:
            suffix = resp.url

        name = '-'.join(
            fix_windir_name(it)
            for it in [
                e.description,
                current_thread().name,
                suffix
            ]
        )

        path = f'{jm_download_dir}/【出错了】{name}.log'
        return path

    def exception_listener(e: JmcomicException):
        """
        异常监听器，实现了在 GitHub Actions 下，把请求错误的信息下载到文件，方便调试和通知使用者
        """
        # 决定要写入的文件路径
        path = decide_filepath(e)

        # 准备内容
        content = [
            str(type(e)),
            e.msg,
        ]
        for k, v in e.context.items():
            content.append(f'{k}: {v}')

        # resp.text
        resp = e.context.get(ExceptionTool.CONTEXT_KEY_RESP, None)
        if resp:
            content.append(f'响应文本: {resp.text}')

        # 写文件
        write_text(path, '\n'.join(content))

    JmModuleConfig.register_exception_listener(JmcomicException, exception_listener)


if __name__ == '__main__':
    main()
