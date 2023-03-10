{
    "targets": [
        {
            "target_name": "cryptonight-hashing",
            "sources": [
                '<!@(uname -a | grep "x86_64" >/dev/null && echo "xmrig/crypto/cn/asm/cn_main_loop.S" || echo)',
                '<!@(uname -a | grep "x86_64" >/dev/null && echo "xmrig/crypto/cn/asm/CryptonightR_template.S" || echo)',
                '<!@(uname -a | grep "x86_64" >/dev/null && echo "xmrig/crypto/cn/r/CryptonightR_gen.cpp" || echo)',
                '<!@(uname -a | grep "x86_64" >/dev/null && (grep avx2 /proc/cpuinfo >/dev/null && echo "xmrig/crypto/cn/gpu/cn_gpu_avx.cpp" || echo) || echo)',
                '<!@(uname -a | grep "x86_64" >/dev/null && echo "xmrig/crypto/cn/gpu/cn_gpu_ssse3.cpp" || echo)',
                '<!@(uname -a | grep "x86_64" >/dev/null || echo "xmrig/crypto/cn/gpu/cn_gpu_arm.cpp" || echo)',
                "multihashing.cc",
                "c29s.cc",
                "c29v.cc",
                "xmrig/crypto/cn/c_blake256.c",
                "xmrig/crypto/cn/c_groestl.c",
                "xmrig/crypto/cn/c_jh.c",
                "xmrig/crypto/cn/c_skein.c",
                "xmrig/base/crypto/keccak.cpp",
                "xmrig/base/crypto/sha3.cpp",
                "xmrig-override/base/crypto/Algorithm.cpp",
                "xmrig/crypto/cn/CnCtx.cpp",
                "xmrig/crypto/cn/CnHash.cpp",
                "xmrig/crypto/common/MemoryPool.cpp",
                "xmrig/crypto/common/VirtualMemory.cpp",
                "xmrig/crypto/common/VirtualMemory_unix.cpp",

                "xmrig/crypto/randomx/aes_hash.cpp",
                "xmrig/crypto/randomx/argon2_ref.c",
                "xmrig/crypto/randomx/bytecode_machine.cpp",
                "xmrig/crypto/randomx/dataset.cpp",
                "xmrig/crypto/randomx/soft_aes.cpp",
                "xmrig/crypto/randomx/virtual_memory.cpp",
                "xmrig/crypto/randomx/vm_interpreted.cpp",
                "xmrig/crypto/randomx/allocator.cpp",
                "xmrig/crypto/randomx/randomx.cpp",
                "xmrig/crypto/randomx/superscalar.cpp",
                "xmrig/crypto/randomx/vm_compiled.cpp",
                "xmrig/crypto/randomx/vm_interpreted_light.cpp",
                "xmrig/crypto/randomx/argon2_core.c",
                "xmrig/crypto/randomx/blake2_generator.cpp",
                "xmrig/crypto/randomx/instructions_portable.cpp",
                "xmrig/crypto/randomx/reciprocal.c",
                "xmrig/crypto/randomx/virtual_machine.cpp",
                "xmrig/crypto/randomx/vm_compiled_light.cpp",
                "xmrig/crypto/randomx/blake2/blake2b.c",
                '<!@(uname -a | grep "x86_64" >/dev/null && echo "xmrig/crypto/randomx/jit_compiler_x86_static.S" || echo)',
                '<!@(uname -a | grep "x86_64" >/dev/null && echo "xmrig/crypto/randomx/jit_compiler_x86.cpp" || echo)',

                "xmrig/3rdparty/argon2/lib/argon2.c",
                "xmrig/3rdparty/argon2/lib/core.c",
                "xmrig/3rdparty/argon2/lib/encoding.c",
                "xmrig/3rdparty/argon2/lib/genkat.c",
                "xmrig/3rdparty/argon2/lib/impl-select.c",
                "xmrig/3rdparty/argon2/lib/blake2/blake2.c",
                '<!@(uname -a | grep "x86_64" >/dev/null && echo "xmrig/3rdparty/argon2/arch/x86_64/lib/argon2-arch.c" || echo)',
                '<!@(uname -a | grep "x86_64" >/dev/null && echo "xmrig/3rdparty/argon2/arch/x86_64/lib/argon2-avx2.c" || echo)',
                '<!@(uname -a | grep "x86_64" >/dev/null && echo "xmrig/3rdparty/argon2/arch/x86_64/lib/argon2-avx512f.c" || echo)',
                '<!@(uname -a | grep "x86_64" >/dev/null && echo "xmrig/3rdparty/argon2/arch/x86_64/lib/argon2-sse2.c" || echo)',
                '<!@(uname -a | grep "x86_64" >/dev/null && echo "xmrig/3rdparty/argon2/arch/x86_64/lib/argon2-ssse3.c" || echo)',
                '<!@(uname -a | grep "x86_64" >/dev/null && echo "xmrig/3rdparty/argon2/arch/x86_64/lib/argon2-xop.c" || echo)',
                '<!@(uname -a | grep "x86_64" >/dev/null && echo "xmrig/3rdparty/argon2/arch/x86_64/lib/cpu-flags.c" || echo)',
                '<!@(uname -a | grep "x86_64" >/dev/null || echo "xmrig/3rdparty/argon2/arch/generic/lib/argon2-arch.c" || echo)',

                "xmrig/crypto/astrobwt/AstroBWT.cpp",
                "xmrig/crypto/astrobwt/Salsa20.cpp",
                "xmrig/crypto/astrobwt/salsa20_ref/salsa20.c",

                "xmrig/crypto/defyx/KangarooTwelve.c",
                "xmrig/crypto/defyx/KeccakP-1600-reference.c",
                "xmrig/crypto/defyx/KeccakSpongeWidth1600.c",
                "xmrig/crypto/defyx/yescrypt-best.c",
                "xmrig/crypto/defyx/sha256.c",

		"xmrig/crypto/kawpow/KPCache.cpp",
		"xmrig/crypto/kawpow/KPHash.cpp",
		"xmrig/3rdparty/libethash/keccakf800.c",
		"xmrig/3rdparty/libethash/ethash_internal.c"
            ],
            "include_dirs": [
                "xmrig-override",
                "xmrig",
                "xmrig/3rdparty/argon2/include",
                "xmrig/3rdparty/argon2/lib",
                "<!(node -e \"require('nan')\")"
            ],
            "cflags_c": [
                '<!@(uname -a | grep "aarch64" >/dev/null && echo "-march=armv8-a+crypto -flax-vector-conversions -DXMRIG_ARM=1" || (uname -a | grep "armv7" >/dev/null && echo "-mfpu=neon -flax-vector-conversions -DXMRIG_ARM=1" || echo "-march=native"))',
                '<!@(grep Intel /proc/cpuinfo >/dev/null && echo -DCPU_INTEL || (grep AMD /proc/cpuinfo >/dev/null && (test `awk \'/cpu family/ && $NF~/^[0-9]*$/ {print $NF}\' /proc/cpuinfo | head -n1` -ge 23 && echo -DCPU_AMD || echo -DCPU_AMD_OLD) || echo))',
                '<!@(grep avx2 /proc/cpuinfo >/dev/null && echo -DHAVE_AVX2 || echo)',
                '<!@(grep sse2 /proc/cpuinfo >/dev/null && echo -DHAVE_SSE2 || echo)',
                '<!@(grep ssse3 /proc/cpuinfo >/dev/null && echo -DHAVE_SSSE3 || echo)',
                '<!@(grep avx512f /proc/cpuinfo >/dev/null && echo -DHAVE_AVX512F || echo)',
                '<!@(grep xop /proc/cpuinfo >/dev/null && echo -DHAVE_XOP || echo)',
                "-std=gnu11      -fPIC -DNDEBUG -Ofast -fno-fast-math -w"
            ],
            "cflags_cc": [
                '<!@(uname -a | grep "aarch64" >/dev/null && echo "-march=armv8-a+crypto -flax-vector-conversions -DXMRIG_ARM=1" || (uname -a | grep "armv7" >/dev/null && echo "-mfpu=neon -flax-vector-conversions -DXMRIG_ARM=1" || echo "-march=native"))',
                '<!@(grep Intel /proc/cpuinfo >/dev/null && echo -DCPU_INTEL || (grep AMD /proc/cpuinfo >/dev/null && (test `awk \'/cpu family/ && $NF~/^[0-9]*$/ {print $NF}\' /proc/cpuinfo | head -n1` -ge 23 && echo -DCPU_AMD || echo -DCPU_AMD_OLD) || echo))',
                "-std=gnu++11 -s -fPIC -DNDEBUG -Ofast -fno-fast-math -fexceptions -fno-rtti -Wno-class-memaccess -w"
            ]
        }
    ]
}
