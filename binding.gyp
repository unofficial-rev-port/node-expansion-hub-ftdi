{
  'targets': [
    {
      'target_name': 'addon',
      'sources': [
        'src/addon.cc',
        'src/EnterFirmwareUpdateMode.cc'
      ],
      'include_dirs': [
        "src/",
        "d2xx/",
        "<!@(node -p \"require('node-addon-api').include\")"
        ],
      'defines': [
        "NAPI_VERSION=<(napi_build_version)"
      ],
      'dependencies': ["<!(node -p \"require('node-addon-api').gyp\")"],
      'link_settings': {
        "conditions": [
          ['OS=="mac"', {
            'libraries': [
                '-l<(module_root_dir)/d2xx/darwin-osxuniversal/libftd2xx.a'
            ]
          }],
          ['OS=="win"', {
            'libraries': [
                '-l<(module_root_dir)/d2xx/win-x64/ftd2xx.lib'
            ]
          }],
          ['OS=="linux"', {
            ['target_arch=="x64"', {
              'libraries': [
                '<(module_root_dir)/d2xx/linux-x64/libftd2xx.so'
            ]}],
            ['target_arch=="arm"', {
              'libraries': [
                '<(module_root_dir)/d2xx/linux-arm32/libftd2xx.so'
            ]}],
            ['target_arch=="arm64"', {
              'libraries': [
                '<(module_root_dir)/d2xx/linux-arm64/libftd2xx.so'
            ]}],
          }]
        ],
      },
      'cflags!': [ '-fno-exceptions' ],
      'cflags_cc!': [ '-fno-exceptions' ],
      'xcode_settings': {
        'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
        'CLANG_CXX_LIBRARY': 'libc++',
        'MACOSX_DEPLOYMENT_TARGET': '10.7'
      },
      'msvs_settings': {
        'VCCLCompilerTool': { 'ExceptionHandling': 1 },
      }
    }
  ],
  'variables' : {
      'openssl_fips': '',
  }
}
