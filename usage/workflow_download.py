from jmcomic import *
from jmcomic.cl import JmcomicUI

# 下方填入你要下载的本子的id，一行一个，每行的首尾可以有空白字符
jm_albums = '''


jm54747
jm28650
jm27512
jm20348
jm47729
jm61257
jm80358
jm18212
jm488125
jm485870
jm181611
jm89218
jm467180
jm480142
jm142464
jm273943
jm401574
jm231692
jm306848
jm371570
jm481979
jm190447
jm409896
jm384297
jm485647
jm495256
jm271249
jm74891
jm2868
jm441594
jm230702
jm284185
jm86779
jm478437
jm21994
jm502132
jm225764
jm352727
jm151696
jm391894
jm392101
jm428347
jm428348
jm148624
jm370634
jm442137
jm438000
jm467110
jm145289
jm505253
jm101792
jm371631
jm305291
jm427706
jm151607
jm505048
jm505484
jm369504
jm501838
jm451610
jm508253
jm355659
jm480841
jm58267
jm69354
jm221659
jm511010
jm145289
jm498750
jm371875
jm465335
jm39509
jm513984
jm452699
jm509489
jm377532
jm517500
jm218796
jm481536
jm515569
jm445794
jm248646
jm326357
jm241726
jm281142
jm290391
jm329995
jm429322
jm411613
jm318731
jm308472
jm105854
jm114445
jm98669
jm73451
jm98509
jm46555
jm27701
jm20106
jm4333
jm2388
jm122333
jm397150
jm394523
jm385372
jm362197
jm346346
jm305428
jm2057
jm333722
jm220455
jm148486
jm486253
jm477990
jm453931
jm452501
jm343898
jm334554
jm318730
jm310176
jm472952
jm203446
jm77778
jm410841
jm412004
jm149906
jm374495
jm346862
jm315728
jm330006
jm290455
jm122427
jm235366
jm265236
jm271249
jm278032
jm487798
jm382336
jm255015
jm230806
jm454803
jm481979
jm434801
jm434797
jm415513
jm477029
jm468624
jm380052
jm269417
jm527354
jm448098
jm509834
jm207063
jm293867
jm192957
jm529468
jm209232
jm181107
jm135697
jm107184
jm127282
jm441189
jm409658
jm116157
jm395281
jm395280
jm392326
jm469738
jm537119
jm542252
jm62268
jm543247
jm368837
jm401496
jm544360
jm544401
jm533552
jm549168
jm471872
jm547590
jm505241
jm392326
jm476677
jm223153
jm21407
jm533458
jm482542
jm433023
jm397478
jm550176
jm125237
jm104738
jm293593
jm303683
jm291407
jm149578
jm124561
jm78665
jm158
jm120944
jm2620
jm45159
jm13660
jm62202
jm262147
jm551529
jm97909
jm239027
jm245952
jm187
jm219
jm224
jm878
jm877
jm759
jm641
jm610
jm638
jm96125
jm390353
jm263104
jm421450
jm543081
jm484683
jm322028
jm303714
jm348168
jm436635
jm417463
jm245189
jm523276
jm443170
jm524360
jm389479
jm224879
jm475378
jm480111
jm411330
jm193267
jm355659
jm345433
jm278435
jm104274
jm435425
jm417420
jm275503
jm342584
jm320765
jm196775
jm229537
jm85055
jm554413
jm541285
jm368639
jm140620
jm21274
jm20902
jm545733
jm541762
jm543525
jm247044
jm55427
jm251050
jm220995
jm33775
jm308595
jm306326
jm50514
jm268453
jm266615
jm249121
jm451603
jm435777
jm355019
jm258778
jm220996
jm142568
jm124116
jm22392
jm479907
jm239797
jm495051
jm501638
jm398569
jm373099
jm138809
jm452452
jm457281
jm338852
jm397036
jm273777
jm381979
jm426538
jm207125
jm508040
jm418181
jm477842
jm343882
jm423216
jm557208
jm85250
jm214052
jm102658
jm96980
jm302226
jm243216
jm308815
jm143400
jm498966
jm561832
jm367583
jm540851
jm552848
jm517017
jm302092
jm218183
jm178548
jm23349
jm499440
jm507124
jm20159
jm40351
jm71804
jm77944
jm103795
jm114104
jm114451
jm163528
jm179339
jm181251
jm187712
jm193267
jm206231
jm212164
jm217593
jm222451
jm229978
jm252238
jm247701
jm251127
jm293430
jm314014
jm341806
jm369749
jm374031
jm399054
jm403167
jm406995
jm413882
jm419674
jm421058
jm442731
jm453568
jm459402
jm464551
jm477691
jm481499
jm485179
jm495582
jm496414
jm509463
jm510795
jm524886
jm530989
jm532871
jm535267
jm537128
jm539454
jm541314
jm542141
jm580890
jm589721
jm589933
jm16921
jm101889
jm203349
jm251948
jm286849
jm369818
jm381566
jm382558
jm411633
jm444162
jm452724
jm477829
jm481316
jm482543
jm494481
jm529624
jm569383
jm475378
jm405521
jm443811
jm332810
jm432651
jm596495
jm596934
jm7zu7
jm47787
jm350234
jm517506
jm558374
jm499731
jm399054
jm501282
jm271925
jm509463
jm529624
jm431206
jm271586
jm540931
jm540836
jm539876
jm535583
jm503149
jm496553
jm481106
jm479374
jm498756
jm482543
jm486483
jm498910
jm416330
jm481972
jm529510
jm499835
jm485581
jm482287
jm527611
jm465141
jm511619
jm478542
jm405698
jm495242
jm527708
jm540931
jm540836
jm539876
jm535583
jm503149
jm496553
jm481106
jm479374
jm498756
jm482543
jm486483
jm498910
jm416330
jm481972
jm529510
jm499835
jm485581
jm482287
jm527611
jm465141
jm511619
jm478542
jm405698
jm495242
jm527708








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
