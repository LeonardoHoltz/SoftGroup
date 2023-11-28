{'training': True,
 '_parameters': OrderedDict(),
 '_buffers': OrderedDict(),
 '_non_persistent_buffers_set': set(),
 '_backward_hooks': OrderedDict(),
 '_is_full_backward_hook': None,
 '_forward_hooks': OrderedDict(),
 '_forward_pre_hooks': OrderedDict(),
 '_state_dict_hooks': OrderedDict(),
 '_load_state_dict_pre_hooks': OrderedDict(),
 '_load_state_dict_post_hooks': OrderedDict(),
 '_modules': OrderedDict([('input_conv',
               SparseSequential(
                 (0): SubMConv3d(6, 32, kernel_size=[3, 3, 3], stride=[1, 1, 1], padding=[1, 1, 1], dilation=[1, 1, 1], output_padding=[0, 0, 0], bias=False, algo=ConvAlgo.MaskImplicitGemm)
               )),
              ('unet',
               UBlock( # lvl 1
                 (blocks): SparseSequential(
                   (block0): ResidualBlock(
                     (i_branch): SparseSequential(
                       (0): Identity()
                     )
                     (conv_branch): SparseSequential(
                       (0): BatchNorm1d(32, eps=0.0001, momentum=0.1, affine=True, track_running_stats=True)
                       (1): ReLU()
                       (2): SubMConv3d(32, 32, kernel_size=[3, 3, 3], stride=[1, 1, 1], padding=[1, 1, 1], dilation=[1, 1, 1], output_padding=[0, 0, 0], bias=False, algo=ConvAlgo.MaskImplicitGemm)
                       (3): BatchNorm1d(32, eps=0.0001, momentum=0.1, affine=True, track_running_stats=True)
                       (4): ReLU()
                       (5): SubMConv3d(32, 32, kernel_size=[3, 3, 3], stride=[1, 1, 1], padding=[1, 1, 1], dilation=[1, 1, 1], output_padding=[0, 0, 0], bias=False, algo=ConvAlgo.MaskImplicitGemm)
                     )
                   )
                   (block1): ResidualBlock(
                     (i_branch): SparseSequential(
                       (0): Identity()
                     )
                     (conv_branch): SparseSequential(
                       (0): BatchNorm1d(32, eps=0.0001, momentum=0.1, affine=True, track_running_stats=True)
                       (1): ReLU()
                       (2): SubMConv3d(32, 32, kernel_size=[3, 3, 3], stride=[1, 1, 1], padding=[1, 1, 1], dilation=[1, 1, 1], output_padding=[0, 0, 0], bias=False, algo=ConvAlgo.MaskImplicitGemm)
                       (3): BatchNorm1d(32, eps=0.0001, momentum=0.1, affine=True, track_running_stats=True)
                       (4): ReLU()
                       (5): SubMConv3d(32, 32, kernel_size=[3, 3, 3], stride=[1, 1, 1], padding=[1, 1, 1], dilation=[1, 1, 1], output_padding=[0, 0, 0], bias=False, algo=ConvAlgo.MaskImplicitGemm)
                     )
                   )
                 )
                 (conv): SparseSequential(
                   (0): BatchNorm1d(32, eps=0.0001, momentum=0.1, affine=True, track_running_stats=True)
                   (1): ReLU()
                   (2): SparseConv3d(32, 64, kernel_size=[2, 2, 2], stride=[2, 2, 2], padding=[0, 0, 0], dilation=[1, 1, 1], output_padding=[0, 0, 0], bias=False, algo=ConvAlgo.MaskImplicitGemm)
                 )
                 (u): UBlock( # lvl 2
                   (blocks): SparseSequential(
                     (block0): ResidualBlock(
                       (i_branch): SparseSequential(
                         (0): Identity()
                       )
                       (conv_branch): SparseSequential(
                         (0): BatchNorm1d(64, eps=0.0001, momentum=0.1, affine=True, track_running_stats=True)
                         (1): ReLU()
                         (2): SubMConv3d(64, 64, kernel_size=[3, 3, 3], stride=[1, 1, 1], padding=[1, 1, 1], dilation=[1, 1, 1], output_padding=[0, 0, 0], bias=False, algo=ConvAlgo.MaskImplicitGemm)
                         (3): BatchNorm1d(64, eps=0.0001, momentum=0.1, affine=True, track_running_stats=True)
                         (4): ReLU()
                         (5): SubMConv3d(64, 64, kernel_size=[3, 3, 3], stride=[1, 1, 1], padding=[1, 1, 1], dilation=[1, 1, 1], output_padding=[0, 0, 0], bias=False, algo=ConvAlgo.MaskImplicitGemm)
                       )
                     )
                     (block1): ResidualBlock(
                       (i_branch): SparseSequential(
                         (0): Identity()
                       )
                       (conv_branch): SparseSequential(
                         (0): BatchNorm1d(64, eps=0.0001, momentum=0.1, affine=True, track_running_stats=True)
                         (1): ReLU()
                         (2): SubMConv3d(64, 64, kernel_size=[3, 3, 3], stride=[1, 1, 1], padding=[1, 1, 1], dilation=[1, 1, 1], output_padding=[0, 0, 0], bias=False, algo=ConvAlgo.MaskImplicitGemm)
                         (3): BatchNorm1d(64, eps=0.0001, momentum=0.1, affine=True, track_running_stats=True)
                         (4): ReLU()
                         (5): SubMConv3d(64, 64, kernel_size=[3, 3, 3], stride=[1, 1, 1], padding=[1, 1, 1], dilation=[1, 1, 1], output_padding=[0, 0, 0], bias=False, algo=ConvAlgo.MaskImplicitGemm)
                       )
                     )
                   )
                   (conv): SparseSequential(
                     (0): BatchNorm1d(64, eps=0.0001, momentum=0.1, affine=True, track_running_stats=True)
                     (1): ReLU()
                     (2): SparseConv3d(64, 96, kernel_size=[2, 2, 2], stride=[2, 2, 2], padding=[0, 0, 0], dilation=[1, 1, 1], output_padding=[0, 0, 0], bias=False, algo=ConvAlgo.MaskImplicitGemm)
                   )
                   (u): UBlock( # lvl 3
                     (blocks): SparseSequential(
                       (block0): ResidualBlock(
                         (i_branch): SparseSequential(
                           (0): Identity()
                         )
                         (conv_branch): SparseSequential(
                           (0): BatchNorm1d(96, eps=0.0001, momentum=0.1, affine=True, track_running_stats=True)
                           (1): ReLU()
                           (2): SubMConv3d(96, 96, kernel_size=[3, 3, 3], stride=[1, 1, 1], padding=[1, 1, 1], dilation=[1, 1, 1], output_padding=[0, 0, 0], bias=False, algo=ConvAlgo.MaskImplicitGemm)
                           (3): BatchNorm1d(96, eps=0.0001, momentum=0.1, affine=True, track_running_stats=True)
                           (4): ReLU()
                           (5): SubMConv3d(96, 96, kernel_size=[3, 3, 3], stride=[1, 1, 1], padding=[1, 1, 1], dilation=[1, 1, 1], output_padding=[0, 0, 0], bias=False, algo=ConvAlgo.MaskImplicitGemm)
                         )
                       )
                       (block1): ResidualBlock(
                         (i_branch): SparseSequential(
                           (0): Identity()
                         )
                         (conv_branch): SparseSequential(
                           (0): BatchNorm1d(96, eps=0.0001, momentum=0.1, affine=True, track_running_stats=True)
                           (1): ReLU()
                           (2): SubMConv3d(96, 96, kernel_size=[3, 3, 3], stride=[1, 1, 1], padding=[1, 1, 1], dilation=[1, 1, 1], output_padding=[0, 0, 0], bias=False, algo=ConvAlgo.MaskImplicitGemm)
                           (3): BatchNorm1d(96, eps=0.0001, momentum=0.1, affine=True, track_running_stats=True)
                           (4): ReLU()
                           (5): SubMConv3d(96, 96, kernel_size=[3, 3, 3], stride=[1, 1, 1], padding=[1, 1, 1], dilation=[1, 1, 1], output_padding=[0, 0, 0], bias=False, algo=ConvAlgo.MaskImplicitGemm)
                         )
                       )
                     )
                     (conv): SparseSequential(
                       (0): BatchNorm1d(96, eps=0.0001, momentum=0.1, affine=True, track_running_stats=True)
                       (1): ReLU()
                       (2): SparseConv3d(96, 128, kernel_size=[2, 2, 2], stride=[2, 2, 2], padding=[0, 0, 0], dilation=[1, 1, 1], output_padding=[0, 0, 0], bias=False, algo=ConvAlgo.MaskImplicitGemm)
                     )
                     (u): UBlock( # lvl 4
                       (blocks): SparseSequential(
                         (block0): ResidualBlock(
                           (i_branch): SparseSequential(
                             (0): Identity()
                           )
                           (conv_branch): SparseSequential(
                             (0): BatchNorm1d(128, eps=0.0001, momentum=0.1, affine=True, track_running_stats=True)
                             (1): ReLU()
                             (2): SubMConv3d(128, 128, kernel_size=[3, 3, 3], stride=[1, 1, 1], padding=[1, 1, 1], dilation=[1, 1, 1], output_padding=[0, 0, 0], bias=False, algo=ConvAlgo.MaskImplicitGemm)
                             (3): BatchNorm1d(128, eps=0.0001, momentum=0.1, affine=True, track_running_stats=True)
                             (4): ReLU()
                             (5): SubMConv3d(128, 128, kernel_size=[3, 3, 3], stride=[1, 1, 1], padding=[1, 1, 1], dilation=[1, 1, 1], output_padding=[0, 0, 0], bias=False, algo=ConvAlgo.MaskImplicitGemm)
                           )
                         )
                         (block1): ResidualBlock(
                           (i_branch): SparseSequential(
                             (0): Identity()
                           )
                           (conv_branch): SparseSequential(
                             (0): BatchNorm1d(128, eps=0.0001, momentum=0.1, affine=True, track_running_stats=True)
                             (1): ReLU()
                             (2): SubMConv3d(128, 128, kernel_size=[3, 3, 3], stride=[1, 1, 1], padding=[1, 1, 1], dilation=[1, 1, 1], output_padding=[0, 0, 0], bias=False, algo=ConvAlgo.MaskImplicitGemm)
                             (3): BatchNorm1d(128, eps=0.0001, momentum=0.1, affine=True, track_running_stats=True)
                             (4): ReLU()
                             (5): SubMConv3d(128, 128, kernel_size=[3, 3, 3], stride=[1, 1, 1], padding=[1, 1, 1], dilation=[1, 1, 1], output_padding=[0, 0, 0], bias=False, algo=ConvAlgo.MaskImplicitGemm)
                           )
                         )
                       )
                       (conv): SparseSequential(
                         (0): BatchNorm1d(128, eps=0.0001, momentum=0.1, affine=True, track_running_stats=True)
                         (1): ReLU()
                         (2): SparseConv3d(128, 160, kernel_size=[2, 2, 2], stride=[2, 2, 2], padding=[0, 0, 0], dilation=[1, 1, 1], output_padding=[0, 0, 0], bias=False, algo=ConvAlgo.MaskImplicitGemm)
                       )
                       (u): UBlock( # lvl 5
                         (blocks): SparseSequential(
                           (block0): ResidualBlock(
                             (i_branch): SparseSequential(
                               (0): Identity()
                             )
                             (conv_branch): SparseSequential(
                               (0): BatchNorm1d(160, eps=0.0001, momentum=0.1, affine=True, track_running_stats=True)
                               (1): ReLU()
                               (2): SubMConv3d(160, 160, kernel_size=[3, 3, 3], stride=[1, 1, 1], padding=[1, 1, 1], dilation=[1, 1, 1], output_padding=[0, 0, 0], bias=False, algo=ConvAlgo.MaskImplicitGemm)
                               (3): BatchNorm1d(160, eps=0.0001, momentum=0.1, affine=True, track_running_stats=True)
                               (4): ReLU()
                               (5): SubMConv3d(160, 160, kernel_size=[3, 3, 3], stride=[1, 1, 1], padding=[1, 1, 1], dilation=[1, 1, 1], output_padding=[0, 0, 0], bias=False, algo=ConvAlgo.MaskImplicitGemm)
                             )
                           )
                           (block1): ResidualBlock(
                             (i_branch): SparseSequential(
                               (0): Identity()
                             )
                             (conv_branch): SparseSequential(
                               (0): BatchNorm1d(160, eps=0.0001, momentum=0.1, affine=True, track_running_stats=True)
                               (1): ReLU()
                               (2): SubMConv3d(160, 160, kernel_size=[3, 3, 3], stride=[1, 1, 1], padding=[1, 1, 1], dilation=[1, 1, 1], output_padding=[0, 0, 0], bias=False, algo=ConvAlgo.MaskImplicitGemm)
                               (3): BatchNorm1d(160, eps=0.0001, momentum=0.1, affine=True, track_running_stats=True)
                               (4): ReLU()
                               (5): SubMConv3d(160, 160, kernel_size=[3, 3, 3], stride=[1, 1, 1], padding=[1, 1, 1], dilation=[1, 1, 1], output_padding=[0, 0, 0], bias=False, algo=ConvAlgo.MaskImplicitGemm)
                             )
                           )
                         )
                         (conv): SparseSequential(
                           (0): BatchNorm1d(160, eps=0.0001, momentum=0.1, affine=True, track_running_stats=True)
                           (1): ReLU()
                           (2): SparseConv3d(160, 192, kernel_size=[2, 2, 2], stride=[2, 2, 2], padding=[0, 0, 0], dilation=[1, 1, 1], output_padding=[0, 0, 0], bias=False, algo=ConvAlgo.MaskImplicitGemm)
                         )
                         (u): UBlock( # lvl 6
                           (blocks): SparseSequential(
                             (block0): ResidualBlock(
                               (i_branch): SparseSequential(
                                 (0): Identity()
                               )
                               (conv_branch): SparseSequential(
                                 (0): BatchNorm1d(192, eps=0.0001, momentum=0.1, affine=True, track_running_stats=True)
                                 (1): ReLU()
                                 (2): SubMConv3d(192, 192, kernel_size=[3, 3, 3], stride=[1, 1, 1], padding=[1, 1, 1], dilation=[1, 1, 1], output_padding=[0, 0, 0], bias=False, algo=ConvAlgo.MaskImplicitGemm)
                                 (3): BatchNorm1d(192, eps=0.0001, momentum=0.1, affine=True, track_running_stats=True)
                                 (4): ReLU()
                                 (5): SubMConv3d(192, 192, kernel_size=[3, 3, 3], stride=[1, 1, 1], padding=[1, 1, 1], dilation=[1, 1, 1], output_padding=[0, 0, 0], bias=False, algo=ConvAlgo.MaskImplicitGemm)
                               )
                             )
                             (block1): ResidualBlock(
                               (i_branch): SparseSequential(
                                 (0): Identity()
                               )
                               (conv_branch): SparseSequential(
                                 (0): BatchNorm1d(192, eps=0.0001, momentum=0.1, affine=True, track_running_stats=True)
                                 (1): ReLU()
                                 (2): SubMConv3d(192, 192, kernel_size=[3, 3, 3], stride=[1, 1, 1], padding=[1, 1, 1], dilation=[1, 1, 1], output_padding=[0, 0, 0], bias=False, algo=ConvAlgo.MaskImplicitGemm)
                                 (3): BatchNorm1d(192, eps=0.0001, momentum=0.1, affine=True, track_running_stats=True)
                                 (4): ReLU()
                                 (5): SubMConv3d(192, 192, kernel_size=[3, 3, 3], stride=[1, 1, 1], padding=[1, 1, 1], dilation=[1, 1, 1], output_padding=[0, 0, 0], bias=False, algo=ConvAlgo.MaskImplicitGemm)
                               )
                             )
                           )
                           (conv): SparseSequential(
                             (0): BatchNorm1d(192, eps=0.0001, momentum=0.1, affine=True, track_running_stats=True)
                             (1): ReLU()
                             (2): SparseConv3d(192, 224, kernel_size=[2, 2, 2], stride=[2, 2, 2], padding=[0, 0, 0], dilation=[1, 1, 1], output_padding=[0, 0, 0], bias=False, algo=ConvAlgo.MaskImplicitGemm)
                           )
                           (u): UBlock( # lvl 7
                             (blocks): SparseSequential(
                               (block0): ResidualBlock(
                                 (i_branch): SparseSequential(
                                   (0): Identity()
                                 )
                                 (conv_branch): SparseSequential(
                                   (0): BatchNorm1d(224, eps=0.0001, momentum=0.1, affine=True, track_running_stats=True)
                                   (1): ReLU()
                                   (2): SubMConv3d(224, 224, kernel_size=[3, 3, 3], stride=[1, 1, 1], padding=[1, 1, 1], dilation=[1, 1, 1], output_padding=[0, 0, 0], bias=False, algo=ConvAlgo.MaskImplicitGemm)
                                   (3): BatchNorm1d(224, eps=0.0001, momentum=0.1, affine=True, track_running_stats=True)
                                   (4): ReLU()
                                   (5): SubMConv3d(224, 224, kernel_size=[3, 3, 3], stride=[1, 1, 1], padding=[1, 1, 1], dilation=[1, 1, 1], output_padding=[0, 0, 0], bias=False, algo=ConvAlgo.MaskImplicitGemm)
                                 )
                               )
                               (block1): ResidualBlock(
                                 (i_branch): SparseSequential(
                                   (0): Identity()
                                 )
                                 (conv_branch): SparseSequential(
                                   (0): BatchNorm1d(224, eps=0.0001, momentum=0.1, affine=True, track_running_stats=True)
                                   (1): ReLU()
                                   (2): SubMConv3d(224, 224, kernel_size=[3, 3, 3], stride=[1, 1, 1], padding=[1, 1, 1], dilation=[1, 1, 1], output_padding=[0, 0, 0], bias=False, algo=ConvAlgo.MaskImplicitGemm)
                                   (3): BatchNorm1d(224, eps=0.0001, momentum=0.1, affine=True, track_running_stats=True)
                                   (4): ReLU()
                                   (5): SubMConv3d(224, 224, kernel_size=[3, 3, 3], stride=[1, 1, 1], padding=[1, 1, 1], dilation=[1, 1, 1], output_padding=[0, 0, 0], bias=False, algo=ConvAlgo.MaskImplicitGemm)
                                 )
                               )
                             )
                           )
                           (deconv): SparseSequential(
                             (0): BatchNorm1d(224, eps=0.0001, momentum=0.1, affine=True, track_running_stats=True)
                             (1): ReLU()
                             (2): SparseInverseConv3d(224, 192, kernel_size=[2, 2, 2], stride=[1, 1, 1], padding=[0, 0, 0], dilation=[1, 1, 1], output_padding=[0, 0, 0], bias=False, algo=ConvAlgo.MaskImplicitGemm)
                           )
                           (blocks_tail): SparseSequential( # lvl 6
                             (block0): ResidualBlock(
                               (i_branch): SparseSequential(
                                 (0): Custom1x1Subm3d(384, 192, kernel_size=[1, 1, 1], stride=[1, 1, 1], padding=[0, 0, 0], dilation=[1, 1, 1], output_padding=[0, 0, 0], bias=False, algo=ConvAlgo.MaskImplicitGemm)
                               )
                               (conv_branch): SparseSequential(
                                 (0): BatchNorm1d(384, eps=0.0001, momentum=0.1, affine=True, track_running_stats=True)
                                 (1): ReLU()
                                 (2): SubMConv3d(384, 192, kernel_size=[3, 3, 3], stride=[1, 1, 1], padding=[1, 1, 1], dilation=[1, 1, 1], output_padding=[0, 0, 0], bias=False, algo=ConvAlgo.MaskImplicitGemm)
                                 (3): BatchNorm1d(192, eps=0.0001, momentum=0.1, affine=True, track_running_stats=True)
                                 (4): ReLU()
                                 (5): SubMConv3d(192, 192, kernel_size=[3, 3, 3], stride=[1, 1, 1], padding=[1, 1, 1], dilation=[1, 1, 1], output_padding=[0, 0, 0], bias=False, algo=ConvAlgo.MaskImplicitGemm)
                               )
                             )
                             (block1): ResidualBlock(
                               (i_branch): SparseSequential(
                                 (0): Identity()
                               )
                               (conv_branch): SparseSequential(
                                 (0): BatchNorm1d(192, eps=0.0001, momentum=0.1, affine=True, track_running_stats=True)
                                 (1): ReLU()
                                 (2): SubMConv3d(192, 192, kernel_size=[3, 3, 3], stride=[1, 1, 1], padding=[1, 1, 1], dilation=[1, 1, 1], output_padding=[0, 0, 0], bias=False, algo=ConvAlgo.MaskImplicitGemm)
                                 (3): BatchNorm1d(192, eps=0.0001, momentum=0.1, affine=True, track_running_stats=True)
                                 (4): ReLU()
                                 (5): SubMConv3d(192, 192, kernel_size=[3, 3, 3], stride=[1, 1, 1], padding=[1, 1, 1], dilation=[1, 1, 1], output_padding=[0, 0, 0], bias=False, algo=ConvAlgo.MaskImplicitGemm)
                               )
                             )
                           )
                         )
                         (deconv): SparseSequential(
                           (0): BatchNorm1d(192, eps=0.0001, momentum=0.1, affine=True, track_running_stats=True)
                           (1): ReLU()
                           (2): SparseInverseConv3d(192, 160, kernel_size=[2, 2, 2], stride=[1, 1, 1], padding=[0, 0, 0], dilation=[1, 1, 1], output_padding=[0, 0, 0], bias=False, algo=ConvAlgo.MaskImplicitGemm)
                         )
                         (blocks_tail): SparseSequential( # lvl 5
                           (block0): ResidualBlock(
                             (i_branch): SparseSequential(
                               (0): Custom1x1Subm3d(320, 160, kernel_size=[1, 1, 1], stride=[1, 1, 1], padding=[0, 0, 0], dilation=[1, 1, 1], output_padding=[0, 0, 0], bias=False, algo=ConvAlgo.MaskImplicitGemm)
                             )
                             (conv_branch): SparseSequential(
                               (0): BatchNorm1d(320, eps=0.0001, momentum=0.1, affine=True, track_running_stats=True)
                               (1): ReLU()
                               (2): SubMConv3d(320, 160, kernel_size=[3, 3, 3], stride=[1, 1, 1], padding=[1, 1, 1], dilation=[1, 1, 1], output_padding=[0, 0, 0], bias=False, algo=ConvAlgo.MaskImplicitGemm)
                               (3): BatchNorm1d(160, eps=0.0001, momentum=0.1, affine=True, track_running_stats=True)
                               (4): ReLU()
                               (5): SubMConv3d(160, 160, kernel_size=[3, 3, 3], stride=[1, 1, 1], padding=[1, 1, 1], dilation=[1, 1, 1], output_padding=[0, 0, 0], bias=False, algo=ConvAlgo.MaskImplicitGemm)
                             )
                           )
                           (block1): ResidualBlock(
                             (i_branch): SparseSequential(
                               (0): Identity()
                             )
                             (conv_branch): SparseSequential(
                               (0): BatchNorm1d(160, eps=0.0001, momentum=0.1, affine=True, track_running_stats=True)
                               (1): ReLU()
                               (2): SubMConv3d(160, 160, kernel_size=[3, 3, 3], stride=[1, 1, 1], padding=[1, 1, 1], dilation=[1, 1, 1], output_padding=[0, 0, 0], bias=False, algo=ConvAlgo.MaskImplicitGemm)
                               (3): BatchNorm1d(160, eps=0.0001, momentum=0.1, affine=True, track_running_stats=True)
                               (4): ReLU()
                               (5): SubMConv3d(160, 160, kernel_size=[3, 3, 3], stride=[1, 1, 1], padding=[1, 1, 1], dilation=[1, 1, 1], output_padding=[0, 0, 0], bias=False, algo=ConvAlgo.MaskImplicitGemm)
                             )
                           )
                         )
                       )
                       (deconv): SparseSequential(
                         (0): BatchNorm1d(160, eps=0.0001, momentum=0.1, affine=True, track_running_stats=True)
                         (1): ReLU()
                         (2): SparseInverseConv3d(160, 128, kernel_size=[2, 2, 2], stride=[1, 1, 1], padding=[0, 0, 0], dilation=[1, 1, 1], output_padding=[0, 0, 0], bias=False, algo=ConvAlgo.MaskImplicitGemm)
                       )
                       (blocks_tail): SparseSequential( # lvl 4
                         (block0): ResidualBlock(
                           (i_branch): SparseSequential(
                             (0): Custom1x1Subm3d(256, 128, kernel_size=[1, 1, 1], stride=[1, 1, 1], padding=[0, 0, 0], dilation=[1, 1, 1], output_padding=[0, 0, 0], bias=False, algo=ConvAlgo.MaskImplicitGemm)
                           )
                           (conv_branch): SparseSequential(
                             (0): BatchNorm1d(256, eps=0.0001, momentum=0.1, affine=True, track_running_stats=True)
                             (1): ReLU()
                             (2): SubMConv3d(256, 128, kernel_size=[3, 3, 3], stride=[1, 1, 1], padding=[1, 1, 1], dilation=[1, 1, 1], output_padding=[0, 0, 0], bias=False, algo=ConvAlgo.MaskImplicitGemm)
                             (3): BatchNorm1d(128, eps=0.0001, momentum=0.1, affine=True, track_running_stats=True)
                             (4): ReLU()
                             (5): SubMConv3d(128, 128, kernel_size=[3, 3, 3], stride=[1, 1, 1], padding=[1, 1, 1], dilation=[1, 1, 1], output_padding=[0, 0, 0], bias=False, algo=ConvAlgo.MaskImplicitGemm)
                           )
                         )
                         (block1): ResidualBlock(
                           (i_branch): SparseSequential(
                             (0): Identity()
                           )
                           (conv_branch): SparseSequential(
                             (0): BatchNorm1d(128, eps=0.0001, momentum=0.1, affine=True, track_running_stats=True)
                             (1): ReLU()
                             (2): SubMConv3d(128, 128, kernel_size=[3, 3, 3], stride=[1, 1, 1], padding=[1, 1, 1], dilation=[1, 1, 1], output_padding=[0, 0, 0], bias=False, algo=ConvAlgo.MaskImplicitGemm)
                             (3): BatchNorm1d(128, eps=0.0001, momentum=0.1, affine=True, track_running_stats=True)
                             (4): ReLU()
                             (5): SubMConv3d(128, 128, kernel_size=[3, 3, 3], stride=[1, 1, 1], padding=[1, 1, 1], dilation=[1, 1, 1], output_padding=[0, 0, 0], bias=False, algo=ConvAlgo.MaskImplicitGemm)
                           )
                         )
                       )
                     )
                     (deconv): SparseSequential(
                       (0): BatchNorm1d(128, eps=0.0001, momentum=0.1, affine=True, track_running_stats=True)
                       (1): ReLU()
                       (2): SparseInverseConv3d(128, 96, kernel_size=[2, 2, 2], stride=[1, 1, 1], padding=[0, 0, 0], dilation=[1, 1, 1], output_padding=[0, 0, 0], bias=False, algo=ConvAlgo.MaskImplicitGemm)
                     )
                     (blocks_tail): SparseSequential( # lvl 3
                       (block0): ResidualBlock(
                         (i_branch): SparseSequential(
                           (0): Custom1x1Subm3d(192, 96, kernel_size=[1, 1, 1], stride=[1, 1, 1], padding=[0, 0, 0], dilation=[1, 1, 1], output_padding=[0, 0, 0], bias=False, algo=ConvAlgo.MaskImplicitGemm)
                         )
                         (conv_branch): SparseSequential(
                           (0): BatchNorm1d(192, eps=0.0001, momentum=0.1, affine=True, track_running_stats=True)
                           (1): ReLU()
                           (2): SubMConv3d(192, 96, kernel_size=[3, 3, 3], stride=[1, 1, 1], padding=[1, 1, 1], dilation=[1, 1, 1], output_padding=[0, 0, 0], bias=False, algo=ConvAlgo.MaskImplicitGemm)
                           (3): BatchNorm1d(96, eps=0.0001, momentum=0.1, affine=True, track_running_stats=True)
                           (4): ReLU()
                           (5): SubMConv3d(96, 96, kernel_size=[3, 3, 3], stride=[1, 1, 1], padding=[1, 1, 1], dilation=[1, 1, 1], output_padding=[0, 0, 0], bias=False, algo=ConvAlgo.MaskImplicitGemm)
                         )
                       )
                       (block1): ResidualBlock(
                         (i_branch): SparseSequential(
                           (0): Identity()
                         )
                         (conv_branch): SparseSequential(
                           (0): BatchNorm1d(96, eps=0.0001, momentum=0.1, affine=True, track_running_stats=True)
                           (1): ReLU()
                           (2): SubMConv3d(96, 96, kernel_size=[3, 3, 3], stride=[1, 1, 1], padding=[1, 1, 1], dilation=[1, 1, 1], output_padding=[0, 0, 0], bias=False, algo=ConvAlgo.MaskImplicitGemm)
                           (3): BatchNorm1d(96, eps=0.0001, momentum=0.1, affine=True, track_running_stats=True)
                           (4): ReLU()
                           (5): SubMConv3d(96, 96, kernel_size=[3, 3, 3], stride=[1, 1, 1], padding=[1, 1, 1], dilation=[1, 1, 1], output_padding=[0, 0, 0], bias=False, algo=ConvAlgo.MaskImplicitGemm)
                         )
                       )
                     )
                   )
                   (deconv): SparseSequential(
                     (0): BatchNorm1d(96, eps=0.0001, momentum=0.1, affine=True, track_running_stats=True)
                     (1): ReLU()
                     (2): SparseInverseConv3d(96, 64, kernel_size=[2, 2, 2], stride=[1, 1, 1], padding=[0, 0, 0], dilation=[1, 1, 1], output_padding=[0, 0, 0], bias=False, algo=ConvAlgo.MaskImplicitGemm)
                   )
                   (blocks_tail): SparseSequential( # lvl 2
                     (block0): ResidualBlock(
                       (i_branch): SparseSequential(
                         (0): Custom1x1Subm3d(128, 64, kernel_size=[1, 1, 1], stride=[1, 1, 1], padding=[0, 0, 0], dilation=[1, 1, 1], output_padding=[0, 0, 0], bias=False, algo=ConvAlgo.MaskImplicitGemm)
                       )
                       (conv_branch): SparseSequential(
                         (0): BatchNorm1d(128, eps=0.0001, momentum=0.1, affine=True, track_running_stats=True)
                         (1): ReLU()
                         (2): SubMConv3d(128, 64, kernel_size=[3, 3, 3], stride=[1, 1, 1], padding=[1, 1, 1], dilation=[1, 1, 1], output_padding=[0, 0, 0], bias=False, algo=ConvAlgo.MaskImplicitGemm)
                         (3): BatchNorm1d(64, eps=0.0001, momentum=0.1, affine=True, track_running_stats=True)
                         (4): ReLU()
                         (5): SubMConv3d(64, 64, kernel_size=[3, 3, 3], stride=[1, 1, 1], padding=[1, 1, 1], dilation=[1, 1, 1], output_padding=[0, 0, 0], bias=False, algo=ConvAlgo.MaskImplicitGemm)
                       )
                     )
                     (block1): ResidualBlock(
                       (i_branch): SparseSequential(
                         (0): Identity()
                       )
                       (conv_branch): SparseSequential(
                         (0): BatchNorm1d(64, eps=0.0001, momentum=0.1, affine=True, track_running_stats=True)
                         (1): ReLU()
                         (2): SubMConv3d(64, 64, kernel_size=[3, 3, 3], stride=[1, 1, 1], padding=[1, 1, 1], dilation=[1, 1, 1], output_padding=[0, 0, 0], bias=False, algo=ConvAlgo.MaskImplicitGemm)
                         (3): BatchNorm1d(64, eps=0.0001, momentum=0.1, affine=True, track_running_stats=True)
                         (4): ReLU()
                         (5): SubMConv3d(64, 64, kernel_size=[3, 3, 3], stride=[1, 1, 1], padding=[1, 1, 1], dilation=[1, 1, 1], output_padding=[0, 0, 0], bias=False, algo=ConvAlgo.MaskImplicitGemm)
                       )
                     )
                   )
                 )
                 (deconv): SparseSequential(
                   (0): BatchNorm1d(64, eps=0.0001, momentum=0.1, affine=True, track_running_stats=True)
                   (1): ReLU()
                   (2): SparseInverseConv3d(64, 32, kernel_size=[2, 2, 2], stride=[1, 1, 1], padding=[0, 0, 0], dilation=[1, 1, 1], output_padding=[0, 0, 0], bias=False, algo=ConvAlgo.MaskImplicitGemm)
                 )
                 (blocks_tail): SparseSequential( # lvl 1
                   (block0): ResidualBlock(
                     (i_branch): SparseSequential(
                       (0): Custom1x1Subm3d(64, 32, kernel_size=[1, 1, 1], stride=[1, 1, 1], padding=[0, 0, 0], dilation=[1, 1, 1], output_padding=[0, 0, 0], bias=False, algo=ConvAlgo.MaskImplicitGemm)
                     )
                     (conv_branch): SparseSequential(
                       (0): BatchNorm1d(64, eps=0.0001, momentum=0.1, affine=True, track_running_stats=True)
                       (1): ReLU()
                       (2): SubMConv3d(64, 32, kernel_size=[3, 3, 3], stride=[1, 1, 1], padding=[1, 1, 1], dilation=[1, 1, 1], output_padding=[0, 0, 0], bias=False, algo=ConvAlgo.MaskImplicitGemm)
                       (3): BatchNorm1d(32, eps=0.0001, momentum=0.1, affine=True, track_running_stats=True)
                       (4): ReLU()
                       (5): SubMConv3d(32, 32, kernel_size=[3, 3, 3], stride=[1, 1, 1], padding=[1, 1, 1], dilation=[1, 1, 1], output_padding=[0, 0, 0], bias=False, algo=ConvAlgo.MaskImplicitGemm)
                     )
                   )
                   (block1): ResidualBlock(
                     (i_branch): SparseSequential(
                       (0): Identity()
                     )
                     (conv_branch): SparseSequential(
                       (0): BatchNorm1d(32, eps=0.0001, momentum=0.1, affine=True, track_running_stats=True)
                       (1): ReLU()
                       (2): SubMConv3d(32, 32, kernel_size=[3, 3, 3], stride=[1, 1, 1], padding=[1, 1, 1], dilation=[1, 1, 1], output_padding=[0, 0, 0], bias=False, algo=ConvAlgo.MaskImplicitGemm)
                       (3): BatchNorm1d(32, eps=0.0001, momentum=0.1, affine=True, track_running_stats=True)
                       (4): ReLU()
                       (5): SubMConv3d(32, 32, kernel_size=[3, 3, 3], stride=[1, 1, 1], padding=[1, 1, 1], dilation=[1, 1, 1], output_padding=[0, 0, 0], bias=False, algo=ConvAlgo.MaskImplicitGemm)
                     )
                   )
                 )
               )),
              ('output_layer',
               SparseSequential(
                 (0): BatchNorm1d(32, eps=0.0001, momentum=0.1, affine=True, track_running_stats=True)
                 (1): ReLU()
               )),
              ('semantic_linear',
               MLP(
                 (0): Linear(in_features=32, out_features=32, bias=True)
                 (1): BatchNorm1d(32, eps=0.0001, momentum=0.1, affine=True, track_running_stats=True)
                 (2): ReLU()
                 (3): Linear(in_features=32, out_features=13, bias=True)
               )),
              ('offset_linear',
               MLP(
                 (0): Linear(in_features=32, out_features=32, bias=True)
                 (1): BatchNorm1d(32, eps=0.0001, momentum=0.1, affine=True, track_running_stats=True)
                 (2): ReLU()
                 (3): Linear(in_features=32, out_features=3, bias=True)
               )),
              ('tiny_unet',
               UBlock(
                 (blocks): SparseSequential(
                   (block0): ResidualBlock(
                     (i_branch): SparseSequential(
                       (0): Identity()
                     )
                     (conv_branch): SparseSequential(
                       (0): BatchNorm1d(32, eps=0.0001, momentum=0.1, affine=True, track_running_stats=True)
                       (1): ReLU()
                       (2): SubMConv3d(32, 32, kernel_size=[3, 3, 3], stride=[1, 1, 1], padding=[1, 1, 1], dilation=[1, 1, 1], output_padding=[0, 0, 0], bias=False, algo=ConvAlgo.MaskImplicitGemm)
                       (3): BatchNorm1d(32, eps=0.0001, momentum=0.1, affine=True, track_running_stats=True)
                       (4): ReLU()
                       (5): SubMConv3d(32, 32, kernel_size=[3, 3, 3], stride=[1, 1, 1], padding=[1, 1, 1], dilation=[1, 1, 1], output_padding=[0, 0, 0], bias=False, algo=ConvAlgo.MaskImplicitGemm)
                     )
                   )
                   (block1): ResidualBlock(
                     (i_branch): SparseSequential(
                       (0): Identity()
                     )
                     (conv_branch): SparseSequential(
                       (0): BatchNorm1d(32, eps=0.0001, momentum=0.1, affine=True, track_running_stats=True)
                       (1): ReLU()
                       (2): SubMConv3d(32, 32, kernel_size=[3, 3, 3], stride=[1, 1, 1], padding=[1, 1, 1], dilation=[1, 1, 1], output_padding=[0, 0, 0], bias=False, algo=ConvAlgo.MaskImplicitGemm)
                       (3): BatchNorm1d(32, eps=0.0001, momentum=0.1, affine=True, track_running_stats=True)
                       (4): ReLU()
                       (5): SubMConv3d(32, 32, kernel_size=[3, 3, 3], stride=[1, 1, 1], padding=[1, 1, 1], dilation=[1, 1, 1], output_padding=[0, 0, 0], bias=False, algo=ConvAlgo.MaskImplicitGemm)
                     )
                   )
                 )
                 (conv): SparseSequential(
                   (0): BatchNorm1d(32, eps=0.0001, momentum=0.1, affine=True, track_running_stats=True)
                   (1): ReLU()
                   (2): SparseConv3d(32, 64, kernel_size=[2, 2, 2], stride=[2, 2, 2], padding=[0, 0, 0], dilation=[1, 1, 1], output_padding=[0, 0, 0], bias=False, algo=ConvAlgo.MaskImplicitGemm)
                 )
                 (u): UBlock(
                   (blocks): SparseSequential(
                     (block0): ResidualBlock(
                       (i_branch): SparseSequential(
                         (0): Identity()
                       )
                       (conv_branch): SparseSequential(
                         (0): BatchNorm1d(64, eps=0.0001, momentum=0.1, affine=True, track_running_stats=True)
                         (1): ReLU()
                         (2): SubMConv3d(64, 64, kernel_size=[3, 3, 3], stride=[1, 1, 1], padding=[1, 1, 1], dilation=[1, 1, 1], output_padding=[0, 0, 0], bias=False, algo=ConvAlgo.MaskImplicitGemm)
                         (3): BatchNorm1d(64, eps=0.0001, momentum=0.1, affine=True, track_running_stats=True)
                         (4): ReLU()
                         (5): SubMConv3d(64, 64, kernel_size=[3, 3, 3], stride=[1, 1, 1], padding=[1, 1, 1], dilation=[1, 1, 1], output_padding=[0, 0, 0], bias=False, algo=ConvAlgo.MaskImplicitGemm)
                       )
                     )
                     (block1): ResidualBlock(
                       (i_branch): SparseSequential(
                         (0): Identity()
                       )
                       (conv_branch): SparseSequential(
                         (0): BatchNorm1d(64, eps=0.0001, momentum=0.1, affine=True, track_running_stats=True)
                         (1): ReLU()
                         (2): SubMConv3d(64, 64, kernel_size=[3, 3, 3], stride=[1, 1, 1], padding=[1, 1, 1], dilation=[1, 1, 1], output_padding=[0, 0, 0], bias=False, algo=ConvAlgo.MaskImplicitGemm)
                         (3): BatchNorm1d(64, eps=0.0001, momentum=0.1, affine=True, track_running_stats=True)
                         (4): ReLU()
                         (5): SubMConv3d(64, 64, kernel_size=[3, 3, 3], stride=[1, 1, 1], padding=[1, 1, 1], dilation=[1, 1, 1], output_padding=[0, 0, 0], bias=False, algo=ConvAlgo.MaskImplicitGemm)
                       )
                     )
                   )
                 )
                 (deconv): SparseSequential(
                   (0): BatchNorm1d(64, eps=0.0001, momentum=0.1, affine=True, track_running_stats=True)
                   (1): ReLU()
                   (2): SparseInverseConv3d(64, 32, kernel_size=[2, 2, 2], stride=[1, 1, 1], padding=[0, 0, 0], dilation=[1, 1, 1], output_padding=[0, 0, 0], bias=False, algo=ConvAlgo.MaskImplicitGemm)
                 )
                 (blocks_tail): SparseSequential(
                   (block0): ResidualBlock(
                     (i_branch): SparseSequential(
                       (0): Custom1x1Subm3d(64, 32, kernel_size=[1, 1, 1], stride=[1, 1, 1], padding=[0, 0, 0], dilation=[1, 1, 1], output_padding=[0, 0, 0], bias=False, algo=ConvAlgo.MaskImplicitGemm)
                     )
                     (conv_branch): SparseSequential(
                       (0): BatchNorm1d(64, eps=0.0001, momentum=0.1, affine=True, track_running_stats=True)
                       (1): ReLU()
                       (2): SubMConv3d(64, 32, kernel_size=[3, 3, 3], stride=[1, 1, 1], padding=[1, 1, 1], dilation=[1, 1, 1], output_padding=[0, 0, 0], bias=False, algo=ConvAlgo.MaskImplicitGemm)
                       (3): BatchNorm1d(32, eps=0.0001, momentum=0.1, affine=True, track_running_stats=True)
                       (4): ReLU()
                       (5): SubMConv3d(32, 32, kernel_size=[3, 3, 3], stride=[1, 1, 1], padding=[1, 1, 1], dilation=[1, 1, 1], output_padding=[0, 0, 0], bias=False, algo=ConvAlgo.MaskImplicitGemm)
                     )
                   )
                   (block1): ResidualBlock(
                     (i_branch): SparseSequential(
                       (0): Identity()
                     )
                     (conv_branch): SparseSequential(
                       (0): BatchNorm1d(32, eps=0.0001, momentum=0.1, affine=True, track_running_stats=True)
                       (1): ReLU()
                       (2): SubMConv3d(32, 32, kernel_size=[3, 3, 3], stride=[1, 1, 1], padding=[1, 1, 1], dilation=[1, 1, 1], output_padding=[0, 0, 0], bias=False, algo=ConvAlgo.MaskImplicitGemm)
                       (3): BatchNorm1d(32, eps=0.0001, momentum=0.1, affine=True, track_running_stats=True)
                       (4): ReLU()
                       (5): SubMConv3d(32, 32, kernel_size=[3, 3, 3], stride=[1, 1, 1], padding=[1, 1, 1], dilation=[1, 1, 1], output_padding=[0, 0, 0], bias=False, algo=ConvAlgo.MaskImplicitGemm)
                     )
                   )
                 )
               )),
              ('tiny_unet_outputlayer',
               SparseSequential(
                 (0): BatchNorm1d(32, eps=0.0001, momentum=0.1, affine=True, track_running_stats=True)
                 (1): ReLU()
               )),
              ('cls_linear',
               Linear(in_features=32, out_features=14, bias=True)),
              ('mask_linear',
               MLP(
                 (0): Linear(in_features=32, out_features=32, bias=True)
                 (1): ReLU()
                 (2): Linear(in_features=32, out_features=14, bias=True)
               )),
              ('iou_score_linear',
               Linear(in_features=32, out_features=14, bias=True))]),
 'in_channels': 6,
 'channels': 32,
 'num_blocks': 7,
 'semantic_only': False,
 'semantic_classes': 13,
 'instance_classes': 13,
 'semantic_weight': None,
 'sem2ins_classes': [0, 1],
 'ignore_label': -100,
 'with_coords': True,
 'grouping_cfg': Munch({'score_thr': 0.2, 'radius': 0.04, 'mean_active': 300, 'class_numpoint_mean': [34229, 39796, 12210, 7457, 5439, 10225, 6016, 1724, 5092, 7424, 5279, 6189, 1823], 'npoint_thr': 0.05, 'ignore_classes': [0, 1]}),
 'instance_voxel_cfg': Munch({'scale': 50, 'spatial_shape': 20}),
 'train_cfg': Munch({'max_proposal_num': 200, 'pos_iou_thr': 0.5}),
 'test_cfg': Munch({'x4_split': True, 'cls_score_thr': 0.001, 'mask_score_thr': -0.5, 'min_npoint': 100, 'eval_tasks': ['semantic', 'instance']}),
 'fixed_modules': ['input_conv',
  'unet',
  'output_layer',
  'semantic_linear',
  'offset_linear']}