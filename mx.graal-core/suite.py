suite = {
  "mxversion" : "5.64.0",
  "name" : "graal-core",

  "imports" : {
    "suites": [
      {
        "name" : "truffle",
        # IMPORTANT: When updating the Truffle import, notify Truffle language developers
        # (by mail to graal-dev@openjdk.java.net) of the pending change.
        "version" : "3895ff0232bbac9d1dfc8eac962906b5e73f6ece",
        "urls" : [
          {"url" : "https://github.com/graalvm/truffle.git", "kind" : "git"},
          {"url" : "https://curio.ssw.jku.at/nexus/content/repositories/snapshots", "kind" : "binary"},
         ]
      },
    ]
  },

  "defaultLicense" : "GPLv2-CPE",

  "jdklibraries" : {
    "JVMCI_SERVICES" : {
      "path" : "lib/jvmci-services.jar",
      "sourcePath" : "lib/jvmci-services.src.zip",
      "optional" : False,
      "jdkStandardizedSince" : "9",
    },
    "JVMCI_API" : {
      "path" : "lib/jvmci/jvmci-api.jar",
      "sourcePath" : "lib/jvmci/jvmci-api.src.zip",
      "dependencies" : [
        "JVMCI_SERVICES",
      ],
      "optional" : False,
      "jdkStandardizedSince" : "9",
    },
    "JVMCI_HOTSPOT" : {
      "path" : "lib/jvmci/jvmci-hotspot.jar",
      "sourcePath" : "lib/jvmci/jvmci-hotspot.src.zip",
      "dependencies" : [
        "JVMCI_API",
      ],
      "optional" : False,
      "jdkStandardizedSince" : "9",
    },
  },

  "libraries" : {

    # ------------- Libraries -------------

    "DACAPO" : {
      "urls" : [
        "https://lafo.ssw.uni-linz.ac.at/pub/graal-external-deps/dacapo-9.12-bach.jar",
        "http://softlayer.dl.sourceforge.net/project/dacapobench/9.12-bach/dacapo-9.12-bach.jar",
      ],
      "sha1" : "2626a9546df09009f6da0df854e6dc1113ef7dd4",
    },

    "DACAPO_SCALA" : {
      "urls" : [
        "https://lafo.ssw.uni-linz.ac.at/pub/graal-external-deps/dacapo-scala-0.1.0-20120216.jar",
        "http://repo.scalabench.org/snapshots/org/scalabench/benchmarks/scala-benchmark-suite/0.1.0-SNAPSHOT/scala-benchmark-suite-0.1.0-20120216.103539-3.jar",
      ],
      "sha1" : "59b64c974662b5cf9dbd3cf9045d293853dd7a51",
    },

    "JAVA_ALLOCATION_INSTRUMENTER" : {
      "urls" : ["https://lafo.ssw.uni-linz.ac.at/pub/java-allocation-instrumenter/java-allocation-instrumenter-8f0db117e64e.jar"],
      "sha1" : "476d9a44cd19d6b55f81571077dfa972a4f8a083",
      "bootClassPathAgent" : "true",
    },

    "HCFDIS" : {
      "urls" : ["https://lafo.ssw.uni-linz.ac.at/pub/hcfdis-3.jar"],
      "sha1" : "a71247c6ddb90aad4abf7c77e501acc60674ef57",
    },

    "C1VISUALIZER_DIST" : {
      "urls" : ["https://lafo.ssw.uni-linz.ac.at/pub/c1visualizer/c1visualizer-1.6.zip"],
      "sha1" : "5309b3fad46067846b9e2ea55933786cdbd6f6dd",
    },

    "IDEALGRAPHVISUALIZER_DIST" : {
      "urls" : ["https://lafo.ssw.uni-linz.ac.at/pub/idealgraphvisualizer/idealgraphvisualizer-8820e1874bf7.zip"],
      "sha1" : "7eb51f6d643ed7833268b6971e273826d44c22b1",
    },

    "JOL_INTERNALS" : {
      "urls" : ["https://lafo.ssw.uni-linz.ac.at/pub/truffle/jol/jol-internals.jar"],
      "sha1" : "508bcd26a4d7c4c44048990c6ea789a3b11a62dc",
    },

    "BATIK" : {
      "sha1" : "122b87ca88e41a415cf8b523fd3d03b4325134a3",
      "urls" : ["https://lafo.ssw.uni-linz.ac.at/pub/graal-external-deps/batik-all-1.7.jar"],
    },
  },

  "projects" : {

    # ------------- NFI -------------

    "com.oracle.nfi" : {
      "subDir" : "graal",
      "sourceDirs" : ["src"],
      "checkstyle" : "org.graalvm.compiler.graph",
      "javaCompliance" : "1.7",
    },

    "com.oracle.nfi.test" : {
      "subDir" : "graal",
      "sourceDirs" : ["test"],
      "dependencies" : [
        "com.oracle.nfi",
        "JVMCI_API",
        "mx:JUNIT",
      ],
      "checkstyle" : "org.graalvm.compiler.graph",
      "javaCompliance" : "1.8",
    },

    # ------------- Graal -------------

    "org.graalvm.compiler.common" : {
      "subDir" : "graal",
      "sourceDirs" : ["src"],
      "dependencies" : ["JVMCI_API"],
      "checkstyle" : "org.graalvm.compiler.graph",
      "javaCompliance" : "1.8",
      "workingSets" : "API,Graal",
    },

    "org.graalvm.compiler.serviceprovider" : {
      "subDir" : "graal",
      "sourceDirs" : ["src"],
      "dependencies" : ["JVMCI_SERVICES"],
      "checkstyle" : "org.graalvm.compiler.graph",
      "javaCompliance" : "1.8",
      "workingSets" : "API,Graal",
    },

    "org.graalvm.compiler.serviceprovider.processor" : {
      "subDir" : "graal",
      "sourceDirs" : ["src"],
      "dependencies" : ["org.graalvm.compiler.serviceprovider"],
      "checkstyle" : "org.graalvm.compiler.graph",
      "javaCompliance" : "1.8",
      "workingSets" : "Graal,Codegen",
    },

    "org.graalvm.compiler.options" : {
      "subDir" : "graal",
      "sourceDirs" : ["src"],
      "checkstyle" : "org.graalvm.compiler.graph",
      "uses" : ["org.graalvm.compiler.options.OptionDescriptors"],
      "javaCompliance" : "1.8",
      "workingSets" : "Graal",
    },

    "org.graalvm.compiler.options.processor" : {
      "subDir" : "graal",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "org.graalvm.compiler.options",
      ],
      "checkstyle" : "org.graalvm.compiler.graph",
      "javaCompliance" : "1.8",
      "workingSets" : "Graal,Codegen",
    },

    "org.graalvm.compiler.options.test" : {
      "subDir" : "graal",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "org.graalvm.compiler.options",
        "mx:JUNIT",
      ],
      "checkstyle" : "org.graalvm.compiler.graph",
      "javaCompliance" : "1.8",
      "workingSets" : "Graal",
    },

    "org.graalvm.compiler.debug" : {
      "subDir" : "graal",
      "sourceDirs" : ["src"],
      "checkstyle" : "org.graalvm.compiler.graph",
      "uses" : [
        "org.graalvm.compiler.debug.DebugConfigCustomizer",
        "org.graalvm.compiler.debug.DebugInitializationParticipant",
        "org.graalvm.compiler.debug.TTYStreamProvider",
      ],
      "dependencies" : [
        "JVMCI_API",
        "org.graalvm.compiler.serviceprovider",
        "org.graalvm.compiler.options"
      ],
      "annotationProcessors" : ["GRAAL_OPTIONS_PROCESSOR"],
      "javaCompliance" : "1.8",
      "workingSets" : "Graal,Debug",
    },

    "org.graalvm.compiler.debug.test" : {
      "subDir" : "graal",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "mx:JUNIT",
        "org.graalvm.compiler.debug",
      ],
      "checkstyle" : "org.graalvm.compiler.graph",
      "javaCompliance" : "1.8",
      "workingSets" : "Graal,Debug,Test",
    },

    "org.graalvm.compiler.code" : {
      "subDir" : "graal",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "org.graalvm.compiler.graph",
        "org.graalvm.compiler.common",
      ],
      "annotationProcessors" : ["GRAAL_SERVICEPROVIDER_PROCESSOR"],
      "checkstyle" : "org.graalvm.compiler.graph",
      "javaCompliance" : "1.8",
      "workingSets" : "Graal",
    },

    "org.graalvm.compiler.api.collections" : {
      "subDir" : "graal",
      "sourceDirs" : ["src"],
      "checkstyle" : "org.graalvm.compiler.graph",
      "javaCompliance" : "1.8",
      "workingSets" : "API,Graal",
    },

    "org.graalvm.compiler.api.directives" : {
      "subDir" : "graal",
      "sourceDirs" : ["src"],
      "checkstyle" : "org.graalvm.compiler.graph",
      "javaCompliance" : "1.8",
      "workingSets" : "API,Graal",
    },

    "org.graalvm.compiler.api.directives.test" : {
      "subDir" : "graal",
      "sourceDirs" : ["src"],
      "checkstyle" : "org.graalvm.compiler.graph",
      "dependencies" : [
        "org.graalvm.compiler.core.test",
        "JVMCI_HOTSPOT",
      ],
      "javaCompliance" : "1.8",
      "workingSets" : "API,Graal",
    },

    "org.graalvm.compiler.api.runtime" : {
      "subDir" : "graal",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "JVMCI_API",
      ],
      "checkstyle" : "org.graalvm.compiler.graph",
      "javaCompliance" : "1.8",
      "workingSets" : "API,Graal",
    },

    "org.graalvm.compiler.api.test" : {
      "subDir" : "graal",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "mx:JUNIT",
        "JVMCI_SERVICES",
        "org.graalvm.compiler.api.runtime",
      ],
      "checkstyle" : "org.graalvm.compiler.graph",
      "javaCompliance" : "1.8",
      "workingSets" : "API,Graal,Test",
    },

    "org.graalvm.compiler.api.replacements" : {
      "subDir" : "graal",
      "sourceDirs" : ["src"],
      "dependencies" : ["JVMCI_API"],
      "checkstyle" : "org.graalvm.compiler.graph",
      "javaCompliance" : "1.8",
      "workingSets" : "API,Graal,Replacements",
    },

    "org.graalvm.compiler.hotspot" : {
      "subDir" : "graal",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "JVMCI_HOTSPOT",
        "org.graalvm.compiler.api.runtime",
        "org.graalvm.compiler.replacements",
        "org.graalvm.compiler.runtime",
      ],
      "imports" : [
        # All other internal packages are exported dynamically -
        # see org.graalvm.compiler.hotspot.HotSpotGraalJVMCIAccess.
        "jdk.internal.module",
      ],
      "checkstyle" : "org.graalvm.compiler.graph",
      "annotationProcessors" : [
        "GRAAL_NODEINFO_PROCESSOR",
        "GRAAL_COMPILER_MATCH_PROCESSOR",
        "GRAAL_REPLACEMENTS_VERIFIER",
        "GRAAL_OPTIONS_PROCESSOR",
        "GRAAL_SERVICEPROVIDER_PROCESSOR",
      ],
      "javaCompliance" : "1.8",
      "workingSets" : "Graal,HotSpot",
    },

    "org.graalvm.compiler.hotspot.aarch64" : {
      "subDir" : "graal",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "org.graalvm.compiler.core.aarch64",
        "org.graalvm.compiler.hotspot",
        "org.graalvm.compiler.replacements.aarch64",
      ],
      "checkstyle" : "org.graalvm.compiler.graph",
      "annotationProcessors" : [
        "GRAAL_SERVICEPROVIDER_PROCESSOR",
        "GRAAL_NODEINFO_PROCESSOR"
      ],
      "javaCompliance" : "1.8",
      "workingSets" : "Graal,HotSpot,AArch64",
    },

    "org.graalvm.compiler.hotspot.amd64" : {
      "subDir" : "graal",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "org.graalvm.compiler.core.amd64",
        "org.graalvm.compiler.hotspot",
        "org.graalvm.compiler.replacements.amd64",
      ],
      "checkstyle" : "org.graalvm.compiler.graph",
      "annotationProcessors" : [
        "GRAAL_SERVICEPROVIDER_PROCESSOR",
        "GRAAL_NODEINFO_PROCESSOR"
      ],
      "javaCompliance" : "1.8",
      "workingSets" : "Graal,HotSpot,AMD64",
    },

    "org.graalvm.compiler.hotspot.sparc" : {
      "subDir" : "graal",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "org.graalvm.compiler.hotspot",
        "org.graalvm.compiler.core.sparc",
        "org.graalvm.compiler.replacements.sparc",
      ],
      "checkstyle" : "org.graalvm.compiler.graph",
      "annotationProcessors" : ["GRAAL_SERVICEPROVIDER_PROCESSOR"],
      "javaCompliance" : "1.8",
      "workingSets" : "Graal,HotSpot,SPARC",
    },

    "org.graalvm.compiler.hotspot.test" : {
      "subDir" : "graal",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "org.graalvm.compiler.replacements.test",
        "org.graalvm.compiler.hotspot",
      ],
      "imports" : [
        "jdk.internal.reflect",
        "jdk.internal.org.objectweb.asm",
      ],
      "annotationProcessors" : ["GRAAL_NODEINFO_PROCESSOR"],
      "checkstyle" : "org.graalvm.compiler.graph",
      "javaCompliance" : "1.8",
      "workingSets" : "Graal,HotSpot,Test",
    },

    "org.graalvm.compiler.hotspot.lir.test" : {
      "subDir" : "graal",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "org.graalvm.compiler.hotspot",
        "org.graalvm.compiler.lir.jtt",
        "org.graalvm.compiler.lir.test",
        "JVMCI_API",
        "JVMCI_HOTSPOT",
      ],
      "checkstyle" : "org.graalvm.compiler.graph",
      "javaCompliance" : "1.8",
      "workingSets" : "Graal,HotSpot,Test",
    },

    "org.graalvm.compiler.hotspot.aarch64.test" : {
      "subDir" : "graal",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "org.graalvm.compiler.asm.aarch64",
        "org.graalvm.compiler.hotspot.test",
      ],
      "annotationProcessors" : ["GRAAL_NODEINFO_PROCESSOR"],
      "checkstyle" : "org.graalvm.compiler.graph",
      "javaCompliance" : "1.8",
      "workingSets" : "Graal,HotSpot,AArch64,Test",
    },

    "org.graalvm.compiler.hotspot.amd64.test" : {
      "subDir" : "graal",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "org.graalvm.compiler.asm.amd64",
        "org.graalvm.compiler.hotspot.test",
        "org.graalvm.compiler.lir.amd64",
        "org.graalvm.compiler.lir.jtt",
      ],
      "annotationProcessors" : ["GRAAL_NODEINFO_PROCESSOR"],
      "checkstyle" : "org.graalvm.compiler.graph",
      "javaCompliance" : "1.8",
      "workingSets" : "Graal,HotSpot,AMD64,Test",
    },

    "org.graalvm.compiler.nodeinfo" : {
      "subDir" : "graal",
      "sourceDirs" : ["src"],
      "checkstyle" : "org.graalvm.compiler.graph",
      "javaCompliance" : "1.8",
      "workingSets" : "Graal,Graph",
    },

    "org.graalvm.compiler.nodeinfo.processor" : {
      "subDir" : "graal",
      "sourceDirs" : ["src"],
      "checkstyle" : "org.graalvm.compiler.graph",
      "dependencies" : [
        "org.graalvm.compiler.nodeinfo",
      ],
      "javaCompliance" : "1.8",
      "workingSets" : "Graal,Graph",
    },

    "org.graalvm.compiler.graph" : {
      "subDir" : "graal",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "org.graalvm.compiler.nodeinfo",
        "org.graalvm.compiler.core.common",
        "org.graalvm.compiler.api.collections",
      ],
      "javaCompliance" : "1.8",
      "annotationProcessors" : [
        "GRAAL_OPTIONS_PROCESSOR",
        "GRAAL_NODEINFO_PROCESSOR"
      ],
      "workingSets" : "Graal,Graph",
    },

    "org.graalvm.compiler.graph.test" : {
      "subDir" : "graal",
      "sourceDirs" : ["src"],
      "checkstyle" : "org.graalvm.compiler.graph",
      "dependencies" : [
        "mx:JUNIT",
        "org.graalvm.compiler.api.test",
        "org.graalvm.compiler.graph",
      ],
      "annotationProcessors" : ["GRAAL_NODEINFO_PROCESSOR"],
      "javaCompliance" : "1.8",
      "workingSets" : "Graal,Graph,Test",
    },

    "org.graalvm.compiler.asm" : {
      "subDir" : "graal",
      "sourceDirs" : ["src"],
      "dependencies" : ["JVMCI_API"],
      "checkstyle" : "org.graalvm.compiler.graph",
      "javaCompliance" : "1.8",
      "workingSets" : "Graal,Assembler",
    },

    "org.graalvm.compiler.asm.aarch64" : {
      "subDir" : "graal",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "org.graalvm.compiler.debug",
        "org.graalvm.compiler.asm",
      ],
      "checkstyle" : "org.graalvm.compiler.graph",
      "javaCompliance" : "1.8",
      "workingSets" : "Graal,Assembler,AArch64",
    },

    "org.graalvm.compiler.asm.amd64" : {
      "subDir" : "graal",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "org.graalvm.compiler.asm",
      ],
      "checkstyle" : "org.graalvm.compiler.graph",
      "javaCompliance" : "1.8",
      "workingSets" : "Graal,Assembler,AMD64",
    },

    "org.graalvm.compiler.asm.sparc" : {
      "subDir" : "graal",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "org.graalvm.compiler.debug",
        "org.graalvm.compiler.asm",
        "org.graalvm.compiler.common"
      ],
      "checkstyle" : "org.graalvm.compiler.graph",
      "javaCompliance" : "1.8",
      "workingSets" : "Graal,Assembler,SPARC",
    },

    "org.graalvm.compiler.asm.sparc.test" : {
      "subDir" : "graal",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "org.graalvm.compiler.asm.test",
        "org.graalvm.compiler.asm.sparc",
      ],
      "checkstyle" : "org.graalvm.compiler.graph",
      "javaCompliance" : "1.8",
      "workingSets" : "Graal,Assembler,SPARC,Test",
    },

    "org.graalvm.compiler.bytecode" : {
      "subDir" : "graal",
      "sourceDirs" : ["src"],
      "dependencies" : ["JVMCI_API"],
      "checkstyle" : "org.graalvm.compiler.graph",
      "javaCompliance" : "1.8",
      "workingSets" : "Graal,Java",
    },

    "org.graalvm.compiler.asm.test" : {
      "subDir" : "graal",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "org.graalvm.compiler.api.test",
        "org.graalvm.compiler.code",
        "org.graalvm.compiler.runtime",
        "org.graalvm.compiler.test",
        "org.graalvm.compiler.debug",
      ],
      "checkstyle" : "org.graalvm.compiler.graph",
      "javaCompliance" : "1.8",
      "workingSets" : "Graal,Assembler,Test",
    },

    "org.graalvm.compiler.asm.aarch64.test" : {
      "subDir" : "graal",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "org.graalvm.compiler.asm.test",
        "org.graalvm.compiler.asm.aarch64",
      ],
      "checkstyle" : "org.graalvm.compiler.graph",
      "javaCompliance" : "1.8",
      "workingSets" : "Graal,Assembler,AArch64,Test",
    },

    "org.graalvm.compiler.asm.amd64.test" : {
      "subDir" : "graal",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "org.graalvm.compiler.asm.test",
        "org.graalvm.compiler.asm.amd64",
      ],
      "checkstyle" : "org.graalvm.compiler.graph",
      "javaCompliance" : "1.8",
      "workingSets" : "Graal,Assembler,AMD64,Test",
    },

    "org.graalvm.compiler.lir" : {
      "subDir" : "graal",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "org.graalvm.compiler.asm",
        "org.graalvm.compiler.code",
      ],
      "annotationProcessors" : ["GRAAL_OPTIONS_PROCESSOR"],
      "checkstyle" : "org.graalvm.compiler.graph",
      "javaCompliance" : "1.8",
      "workingSets" : "Graal,LIR",
    },

    "org.graalvm.compiler.lir.jtt" : {
      "subDir" : "graal",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "org.graalvm.compiler.jtt",
      ],
      "annotationProcessors" : ["GRAAL_NODEINFO_PROCESSOR"],
      "checkstyle" : "org.graalvm.compiler.graph",
      "javaCompliance" : "1.8",
      "workingSets" : "Graal,LIR",
      "findbugs" : "false",
    },

    "org.graalvm.compiler.lir.test" : {
      "subDir" : "graal",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "mx:JUNIT",
        "org.graalvm.compiler.lir",
      ],
      "checkstyle" : "org.graalvm.compiler.graph",
      "javaCompliance" : "1.8",
      "workingSets" : "Graal,LIR",
    },

    "org.graalvm.compiler.lir.aarch64" : {
      "subDir" : "graal",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "org.graalvm.compiler.lir",
        "org.graalvm.compiler.asm.aarch64",
      ],
      "annotationProcessors" : ["GRAAL_OPTIONS_PROCESSOR"],
      "checkstyle" : "org.graalvm.compiler.graph",
      "javaCompliance" : "1.8",
      "workingSets" : "Graal,LIR,AArch64",
    },

    "org.graalvm.compiler.lir.amd64" : {
      "subDir" : "graal",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "org.graalvm.compiler.lir",
        "org.graalvm.compiler.asm.amd64",
      ],
      "annotationProcessors" : ["GRAAL_OPTIONS_PROCESSOR"],
      "checkstyle" : "org.graalvm.compiler.graph",
      "javaCompliance" : "1.8",
      "workingSets" : "Graal,LIR,AMD64",
    },

    "org.graalvm.compiler.lir.sparc" : {
      "subDir" : "graal",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "org.graalvm.compiler.asm.sparc",
        "org.graalvm.compiler.lir",
      ],
      "checkstyle" : "org.graalvm.compiler.graph",
      "javaCompliance" : "1.8",
      "workingSets" : "Graal,LIR,SPARC",
    },

    "org.graalvm.compiler.word" : {
      "subDir" : "graal",
      "sourceDirs" : ["src"],
      "dependencies" : ["org.graalvm.compiler.nodes"],
      "checkstyle" : "org.graalvm.compiler.graph",
      "javaCompliance" : "1.8",
      "annotationProcessors" : ["GRAAL_NODEINFO_PROCESSOR"],
      "workingSets" : "API,Graal",
    },

    "org.graalvm.compiler.replacements" : {
      "subDir" : "graal",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "org.graalvm.compiler.api.directives",
        "org.graalvm.compiler.java",
        "org.graalvm.compiler.loop.phases",
        "org.graalvm.compiler.word",
      ],
      "checkstyle" : "org.graalvm.compiler.graph",
      "javaCompliance" : "1.8",
      "annotationProcessors" : [
        "GRAAL_OPTIONS_PROCESSOR",
        "GRAAL_REPLACEMENTS_VERIFIER",
        "GRAAL_NODEINFO_PROCESSOR",
      ],
      "workingSets" : "Graal,Replacements",
    },

    "org.graalvm.compiler.replacements.aarch64" : {
      "subDir" : "graal",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "org.graalvm.compiler.replacements",
        "org.graalvm.compiler.lir.aarch64",
      ],
      "checkstyle" : "org.graalvm.compiler.graph",
      "javaCompliance" : "1.8",
      "annotationProcessors" : [
        "GRAAL_NODEINFO_PROCESSOR",
        "GRAAL_REPLACEMENTS_VERIFIER",
      ],
      "workingSets" : "Graal,Replacements,AArch64",
    },

    "org.graalvm.compiler.replacements.amd64" : {
      "subDir" : "graal",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "org.graalvm.compiler.replacements",
        "org.graalvm.compiler.lir.amd64",
      ],
      "checkstyle" : "org.graalvm.compiler.graph",
      "javaCompliance" : "1.8",
      "annotationProcessors" : [
        "GRAAL_NODEINFO_PROCESSOR",
        "GRAAL_REPLACEMENTS_VERIFIER",
      ],
      "workingSets" : "Graal,Replacements,AMD64",
    },

    "org.graalvm.compiler.replacements.sparc" : {
      "subDir" : "graal",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "org.graalvm.compiler.replacements",
      ],
      "checkstyle" : "org.graalvm.compiler.graph",
      "javaCompliance" : "1.8",
      "workingSets" : "Graal,Replacements,SPARC",
    },

    "org.graalvm.compiler.replacements.test" : {
      "subDir" : "graal",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "org.graalvm.compiler.core.test",
        "org.graalvm.compiler.replacements",
      ],
      "annotationProcessors" : [
        "GRAAL_NODEINFO_PROCESSOR",
        "GRAAL_REPLACEMENTS_VERIFIER"
      ],
      "checkstyle" : "org.graalvm.compiler.graph",
      "javaCompliance" : "1.8",
      "workingSets" : "Graal,Replacements,Test",
      "jacoco" : "exclude",
    },

    "org.graalvm.compiler.replacements.verifier" : {
      "subDir" : "graal",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "org.graalvm.compiler.api.replacements",
        "org.graalvm.compiler.graph",
      ],
      "checkstyle" : "org.graalvm.compiler.graph",
      "javaCompliance" : "1.8",
      "workingSets" : "Graal,Replacements",
    },

    "org.graalvm.compiler.nodes" : {
      "subDir" : "graal",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "org.graalvm.compiler.api.replacements",
        "org.graalvm.compiler.bytecode",
        "org.graalvm.compiler.lir",
      ],
      "checkstyle" : "org.graalvm.compiler.graph",
      "javaCompliance" : "1.8",
      "annotationProcessors" : [
        "GRAAL_NODEINFO_PROCESSOR",
        "GRAAL_REPLACEMENTS_VERIFIER",
      ],
      "workingSets" : "Graal,Graph",
    },

    "org.graalvm.compiler.nodes.test" : {
      "subDir" : "graal",
      "sourceDirs" : ["src"],
      "dependencies" : ["org.graalvm.compiler.core.test"],
      "checkstyle" : "org.graalvm.compiler.graph",
      "javaCompliance" : "1.8",
      "workingSets" : "Graal,Graph",
    },

    "org.graalvm.compiler.phases" : {
      "subDir" : "graal",
      "sourceDirs" : ["src"],
      "dependencies" : ["org.graalvm.compiler.nodes"],
      "annotationProcessors" : ["GRAAL_OPTIONS_PROCESSOR"],
      "checkstyle" : "org.graalvm.compiler.graph",
      "javaCompliance" : "1.8",
      "workingSets" : "Graal,Phases",
    },

    "org.graalvm.compiler.phases.common" : {
      "subDir" : "graal",
      "sourceDirs" : ["src"],
      "dependencies" : ["org.graalvm.compiler.phases"],
      "annotationProcessors" : [
        "GRAAL_NODEINFO_PROCESSOR",
        "GRAAL_OPTIONS_PROCESSOR"
      ],
      "checkstyle" : "org.graalvm.compiler.graph",
      "javaCompliance" : "1.8",
      "workingSets" : "Graal,Phases",
    },

    "org.graalvm.compiler.phases.common.test" : {
      "subDir" : "graal",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "org.graalvm.compiler.api.test",
        "org.graalvm.compiler.runtime",
        "mx:JUNIT",
      ],
      "checkstyle" : "org.graalvm.compiler.graph",
      "javaCompliance" : "1.8",
      "workingSets" : "Graal,Test",
    },

    "org.graalvm.compiler.virtual" : {
      "subDir" : "graal",
      "sourceDirs" : ["src"],
      "dependencies" : ["org.graalvm.compiler.phases.common"],
      "annotationProcessors" : [
        "GRAAL_OPTIONS_PROCESSOR",
        "GRAAL_NODEINFO_PROCESSOR"
      ],
      "checkstyle" : "org.graalvm.compiler.graph",
      "javaCompliance" : "1.8",
      "workingSets" : "Graal,Phases",
    },

    "org.graalvm.compiler.virtual.bench" : {
      "subDir" : "graal",
      "sourceDirs" : ["src"],
      "dependencies" : ["mx:JMH", "org.graalvm.compiler.microbenchmarks"],
      "checkstyle" : "org.graalvm.compiler.graph",
      "javaCompliance" : "1.8",
      "annotationProcessors" : ["mx:JMH"],
      "workingSets" : "Graal,Bench",
    },

    "org.graalvm.compiler.microbenchmarks" : {
      "subDir" : "graal",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "mx:JMH",
        "org.graalvm.compiler.api.test",
        "org.graalvm.compiler.java",
        "org.graalvm.compiler.runtime",
      ],
      "checkstyle" : "org.graalvm.compiler.graph",
      "javaCompliance" : "1.8",
      "checkPackagePrefix" : "false",
      "annotationProcessors" : ["mx:JMH"],
      "workingSets" : "Graal,Bench",
    },

    "org.graalvm.compiler.loop" : {
      "subDir" : "graal",
      "sourceDirs" : ["src"],
      "dependencies" : ["org.graalvm.compiler.nodes"],
      "annotationProcessors" : ["GRAAL_OPTIONS_PROCESSOR"],
      "checkstyle" : "org.graalvm.compiler.graph",
      "javaCompliance" : "1.8",
      "workingSets" : "Graal",
    },

    "org.graalvm.compiler.loop.phases" : {
      "subDir" : "graal",
      "sourceDirs" : ["src"],
      "dependencies" : [
     "org.graalvm.compiler.loop",
     "org.graalvm.compiler.phases.common",
       ],
      "annotationProcessors" : ["GRAAL_OPTIONS_PROCESSOR"],
      "checkstyle" : "org.graalvm.compiler.graph",
      "javaCompliance" : "1.8",
      "workingSets" : "Graal,Phases",
    },

    "org.graalvm.compiler.core" : {
      "subDir" : "graal",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "org.graalvm.compiler.virtual",
        "org.graalvm.compiler.loop.phases",
      ],
      "uses" : ["org.graalvm.compiler.core.match.MatchStatementSet"],
      "checkstyle" : "org.graalvm.compiler.graph",
      "javaCompliance" : "1.8",
      "annotationProcessors" : [
        "GRAAL_SERVICEPROVIDER_PROCESSOR",
        "GRAAL_OPTIONS_PROCESSOR",
      ],
      "workingSets" : "Graal",
    },

    "org.graalvm.compiler.core.match.processor" : {
      "subDir" : "graal",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "org.graalvm.compiler.core",
      ],
      "checkstyle" : "org.graalvm.compiler.graph",
      "javaCompliance" : "1.8",
      "workingSets" : "Graal,Codegen",
    },

    "org.graalvm.compiler.core.aarch64" : {
      "subDir" : "graal",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "org.graalvm.compiler.core",
        "org.graalvm.compiler.lir.aarch64",
        "org.graalvm.compiler.java",
      ],
      "checkstyle" : "org.graalvm.compiler.graph",
      "annotationProcessors" : [
        "GRAAL_NODEINFO_PROCESSOR",
        "GRAAL_COMPILER_MATCH_PROCESSOR",
      ],
      "javaCompliance" : "1.8",
      "workingSets" : "Graal,AArch64",
    },

    "org.graalvm.compiler.core.aarch64.test" : {
      "subDir" : "graal",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "org.graalvm.compiler.lir.jtt",
        "org.graalvm.compiler.lir.aarch64",
        "JVMCI_HOTSPOT"
      ],
      "checkstyle" : "org.graalvm.compiler.graph",
      "javaCompliance" : "1.8",
      "workingSets" : "Graal,AArch64,Test",
    },

    "org.graalvm.compiler.core.amd64" : {
      "subDir" : "graal",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "org.graalvm.compiler.core",
        "org.graalvm.compiler.lir.amd64",
        "org.graalvm.compiler.java",
      ],
      "checkstyle" : "org.graalvm.compiler.graph",
      "annotationProcessors" : [
        "GRAAL_NODEINFO_PROCESSOR",
        "GRAAL_COMPILER_MATCH_PROCESSOR",
      ],
      "javaCompliance" : "1.8",
      "workingSets" : "Graal,AMD64",
    },

    "org.graalvm.compiler.core.amd64.test" : {
      "subDir" : "graal",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "org.graalvm.compiler.lir.jtt",
        "org.graalvm.compiler.lir.amd64",
        "JVMCI_HOTSPOT"
      ],
      "checkstyle" : "org.graalvm.compiler.graph",
      "javaCompliance" : "1.8",
      "workingSets" : "Graal,AMD64,Test",
    },

    "org.graalvm.compiler.core.sparc" : {
      "subDir" : "graal",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "org.graalvm.compiler.core",
        "org.graalvm.compiler.lir.sparc",
        "org.graalvm.compiler.java"
      ],
      "checkstyle" : "org.graalvm.compiler.graph",
      "annotationProcessors" : [
        "GRAAL_NODEINFO_PROCESSOR",
        "GRAAL_COMPILER_MATCH_PROCESSOR",
      ],
      "javaCompliance" : "1.8",
      "workingSets" : "Graal,SPARC",
    },

    "org.graalvm.compiler.core.sparc.test" : {
      "subDir" : "graal",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "org.graalvm.compiler.lir.jtt",
        "JVMCI_HOTSPOT"
      ],
      "checkstyle" : "org.graalvm.compiler.graph",
      "javaCompliance" : "1.8",
      "workingSets" : "Graal,SPARC,Test",
    },

    "org.graalvm.compiler.runtime" : {
      "subDir" : "graal",
      "sourceDirs" : ["src"],
      "dependencies" : ["org.graalvm.compiler.core"],
      "checkstyle" : "org.graalvm.compiler.graph",
      "javaCompliance" : "1.8",
      "workingSets" : "Graal",
    },

    "org.graalvm.compiler.java" : {
      "subDir" : "graal",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "org.graalvm.compiler.phases",
      ],
      "annotationProcessors" : ["GRAAL_OPTIONS_PROCESSOR"],
      "checkstyle" : "org.graalvm.compiler.graph",
      "javaCompliance" : "1.8",
      "workingSets" : "Graal,Java",
    },

    "org.graalvm.compiler.core.common" : {
      "subDir" : "graal",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "org.graalvm.compiler.debug"
      ],
      "annotationProcessors" : ["GRAAL_OPTIONS_PROCESSOR"],
      "checkstyle" : "org.graalvm.compiler.graph",
      "javaCompliance" : "1.8",
      "workingSets" : "Graal,Java",
    },

    "org.graalvm.compiler.printer" : {
      "subDir" : "graal",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "org.graalvm.compiler.core",
        "org.graalvm.compiler.java",
      ],
      "uses" : ["org.graalvm.compiler.code.DisassemblerProvider"],
      "annotationProcessors" : [
        "GRAAL_OPTIONS_PROCESSOR",
        "GRAAL_SERVICEPROVIDER_PROCESSOR"
      ],
      "checkstyle" : "org.graalvm.compiler.graph",
      "javaCompliance" : "1.8",
      "workingSets" : "Graal,Graph",
    },

    "org.graalvm.compiler.test" : {
      "subDir" : "graal",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "mx:JUNIT",
      ],
      "checkstyle" : "org.graalvm.compiler.graph",
      "javaCompliance" : "1.8",
      "workingSets" : "Graal,Test",
    },

    "org.graalvm.compiler.core.test" : {
      "subDir" : "graal",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "org.graalvm.compiler.api.directives",
        "org.graalvm.compiler.java",
        "org.graalvm.compiler.test",
        "org.graalvm.compiler.runtime",
        "org.graalvm.compiler.graph.test",
        "org.graalvm.compiler.printer",
        "JAVA_ALLOCATION_INSTRUMENTER",
      ],
      "uses" : ["org.graalvm.compiler.options.OptionDescriptors"],
      "annotationProcessors" : ["GRAAL_NODEINFO_PROCESSOR"],
      "checkstyle" : "org.graalvm.compiler.graph",
      "javaCompliance" : "1.8",
      "workingSets" : "Graal,Test",
      "jacoco" : "exclude",
    },

    "org.graalvm.compiler.jtt" : {
      "subDir" : "graal",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "org.graalvm.compiler.core.test",
      ],
      "checkstyle" : "org.graalvm.compiler.graph",
      "javaCompliance" : "1.8",
      "workingSets" : "Graal,Test",
      "jacoco" : "exclude",
      "findbugs" : "false",
    },

    # ------------- GraalTruffle -------------

    "org.graalvm.compiler.truffle" : {
      "subDir" : "graal",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "truffle:TRUFFLE_API",
        "org.graalvm.compiler.api.runtime",
        "org.graalvm.compiler.runtime",
        "org.graalvm.compiler.replacements",
      ],
      "uses" : [
        "com.oracle.truffle.api.object.LayoutFactory",
        "org.graalvm.compiler.truffle.LoopNodeFactory",
        "org.graalvm.compiler.truffle.substitutions.TruffleInvocationPluginProvider",
      ],
      "checkstyle" : "org.graalvm.compiler.graph",
      "annotationProcessors" : [
        "GRAAL_NODEINFO_PROCESSOR",
        "GRAAL_REPLACEMENTS_VERIFIER",
        "GRAAL_OPTIONS_PROCESSOR",
        "GRAAL_SERVICEPROVIDER_PROCESSOR",
        "truffle:TRUFFLE_DSL_PROCESSOR",
      ],
      "javaCompliance" : "1.8",
      "workingSets" : "Graal,Truffle",
      "jacoco" : "exclude",
    },

    "org.graalvm.compiler.truffle.bench" : {
      "subDir" : "graal",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "mx:JMH",
        "truffle:TRUFFLE_API",
      ],
      "checkstyle" : "org.graalvm.compiler.graph",
      "javaCompliance" : "1.8",
      "annotationProcessors" : [
        "mx:JMH",
      ],
      "workingSets" : "Graal,Truffle,Bench",
    },

    "org.graalvm.compiler.truffle.test" : {
      "subDir" : "graal",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "org.graalvm.compiler.truffle",
        "org.graalvm.compiler.core.test",
        "truffle:TRUFFLE_SL_TEST",
      ],
      "annotationProcessors" : [
        "GRAAL_NODEINFO_PROCESSOR",
        "truffle:TRUFFLE_DSL_PROCESSOR"
      ],
      "checkstyle" : "org.graalvm.compiler.graph",
      "javaCompliance" : "1.8",
      "workingSets" : "Graal,Truffle,Test",
      "jacoco" : "exclude",
    },

    "org.graalvm.compiler.truffle.hotspot" : {
      "subDir" : "graal",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "org.graalvm.compiler.truffle",
        "org.graalvm.compiler.hotspot",
        "com.oracle.nfi",
      ],
      "uses" : [
        "org.graalvm.compiler.hotspot.HotSpotBackendFactory",
        "org.graalvm.compiler.nodes.graphbuilderconf.NodeIntrinsicPluginFactory",
        "org.graalvm.compiler.truffle.hotspot.OptimizedCallTargetInstrumentationFactory",
        "org.graalvm.compiler.truffle.hotspot.nfi.RawNativeCallNodeFactory",
      ],
      "checkstyle" : "org.graalvm.compiler.graph",
      "javaCompliance" : "1.8",
      "annotationProcessors" : [
        "GRAAL_OPTIONS_PROCESSOR",
        "GRAAL_SERVICEPROVIDER_PROCESSOR"
      ],
      "workingSets" : "Graal,Truffle",
    },

    "org.graalvm.compiler.truffle.hotspot.test" : {
      "subDir" : "graal",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "org.graalvm.compiler.truffle.hotspot",
        "org.graalvm.compiler.truffle.test",
      ],
      "checkstyle" : "org.graalvm.compiler.graph",
      "javaCompliance" : "1.8",
      "workingSets" : "Graal,Truffle,Test",
    },

    "org.graalvm.compiler.truffle.hotspot.amd64" : {
      "subDir" : "graal",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "org.graalvm.compiler.truffle.hotspot",
        "org.graalvm.compiler.hotspot.amd64",
      ],
      "checkstyle" : "org.graalvm.compiler.graph",
      "javaCompliance" : "1.8",
      "annotationProcessors" : [
        "GRAAL_SERVICEPROVIDER_PROCESSOR",
      ],
      "workingSets" : "Graal,Truffle",
    },

    "org.graalvm.compiler.truffle.hotspot.sparc" : {
      "subDir" : "graal",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "org.graalvm.compiler.truffle.hotspot",
        "org.graalvm.compiler.asm.sparc",
      ],
      "checkstyle" : "org.graalvm.compiler.graph",
      "javaCompliance" : "1.8",
      "annotationProcessors" : ["GRAAL_SERVICEPROVIDER_PROCESSOR"],
      "workingSets" : "Graal,Truffle,SPARC",
    },

    "org.graalvm.compiler.truffle.hotspot.aarch64" : {
      "subDir" : "graal",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "org.graalvm.compiler.truffle.hotspot",
        "org.graalvm.compiler.asm.aarch64",
      ],
      "checkstyle" : "org.graalvm.compiler.graph",
      "javaCompliance" : "1.8",
      "annotationProcessors" : ["GRAAL_SERVICEPROVIDER_PROCESSOR"],
      "workingSets" : "Graal,Truffle,AArch64",
    },

    # ------------- Salver -------------

    "org.graalvm.compiler.salver" : {
      "subDir" : "graal",
      "sourceDirs" : ["src"],
      "dependencies" : ["org.graalvm.compiler.phases"],
      "annotationProcessors" : [
        "GRAAL_OPTIONS_PROCESSOR",
        "GRAAL_SERVICEPROVIDER_PROCESSOR",
      ],
      "checkstyle" : "org.graalvm.compiler.graph",
      "javaCompliance" : "1.8",
      "workingSets" : "Graal",
    },
  },

  "distributions" : {

    # ------------- Distributions -------------

    "GRAAL_OPTIONS" : {
      "subDir" : "graal",
      "dependencies" : ["org.graalvm.compiler.options"],
      "distDependencies" : [
        "JVMCI_API",
      ],
    },

    "GRAAL_OPTIONS_PROCESSOR" : {
      "subDir" : "graal",
      "dependencies" : ["org.graalvm.compiler.options.processor"],
      "distDependencies" : [
        "GRAAL_OPTIONS",
      ],
    },

    "GRAAL_NODEINFO" : {
      "subDir" : "graal",
      "dependencies" : [
        "org.graalvm.compiler.nodeinfo",
      ],
    },

    "GRAAL_SERVICEPROVIDER" : {
      "subDir" : "graal",
      "dependencies" : ["org.graalvm.compiler.serviceprovider"],
      "distDependencies" : [
        "GRAAL_NODEINFO",
        "JVMCI_SERVICES"
      ],
    },

    "GRAAL_API" : {
      "subDir" : "graal",
      "dependencies" : [
        "org.graalvm.compiler.api.replacements",
        "org.graalvm.compiler.api.runtime",
        "org.graalvm.compiler.graph",
      ],
      "distDependencies" : [
        "JVMCI_API",
        "GRAAL_NODEINFO",
        "GRAAL_OPTIONS",
        "GRAAL_SERVICEPROVIDER",
      ],
    },

    "GRAAL_COMPILER" : {
      "subDir" : "graal",
      "dependencies" : [
        "org.graalvm.compiler.core",
      ],
      "distDependencies" : [
        "GRAAL_API",
        "GRAAL_SERVICEPROVIDER",
      ],
    },

    "GRAAL_RUNTIME" : {
      "subDir" : "graal",
      "dependencies" : [
        "org.graalvm.compiler.replacements",
        "org.graalvm.compiler.runtime",
        "org.graalvm.compiler.code",
        "org.graalvm.compiler.printer",
        "org.graalvm.compiler.core.aarch64",
        "org.graalvm.compiler.replacements.aarch64",
        "org.graalvm.compiler.core.amd64",
        "org.graalvm.compiler.replacements.amd64",
        "org.graalvm.compiler.core.sparc",
        "org.graalvm.compiler.replacements.sparc",
        "org.graalvm.compiler.salver",
      ],
      "distDependencies" : [
        "GRAAL_API",
        "GRAAL_COMPILER",
      ],
    },

    "GRAAL_HOTSPOT" : {
      "subDir" : "graal",
      "dependencies" : [
        "org.graalvm.compiler.hotspot.aarch64",
        "org.graalvm.compiler.hotspot.amd64",
        "org.graalvm.compiler.hotspot.sparc",
        "org.graalvm.compiler.hotspot",
      ],
      "distDependencies" : [
        "JVMCI_HOTSPOT",
        "GRAAL_COMPILER",
        "GRAAL_RUNTIME",
      ],
    },

    "GRAAL_TEST" : {
      "subDir" : "graal",
      "dependencies" : [
        "org.graalvm.compiler.api.test",
        "org.graalvm.compiler.api.directives.test",
        "org.graalvm.compiler.asm.sparc.test",
        "org.graalvm.compiler.asm.aarch64.test",
        "org.graalvm.compiler.asm.amd64.test",
        "org.graalvm.compiler.core.aarch64.test",
        "org.graalvm.compiler.core.amd64.test",
        "org.graalvm.compiler.core.sparc.test",
        "org.graalvm.compiler.debug.test",
        "org.graalvm.compiler.hotspot.aarch64.test",
        "org.graalvm.compiler.hotspot.amd64.test",
        "org.graalvm.compiler.hotspot.lir.test",
        "org.graalvm.compiler.options.test",
        "org.graalvm.compiler.jtt",
        "org.graalvm.compiler.lir.jtt",
        "org.graalvm.compiler.lir.test",
        "org.graalvm.compiler.nodes.test",
        "org.graalvm.compiler.phases.common.test",
        "org.graalvm.compiler.truffle.test",
        "org.graalvm.compiler.truffle.hotspot.test",
        "com.oracle.nfi.test",
      ],
      "distDependencies" : [
        "GRAAL_HOTSPOT",
        "JVMCI_HOTSPOT",
        "GRAAL_TRUFFLE",
        "GRAAL_TRUFFLE_HOTSPOT",
        "truffle:TRUFFLE_SL_TEST",
      ],
      "exclude" : [
        "mx:JUNIT",
        "JAVA_ALLOCATION_INSTRUMENTER",
      ],
    },

    "GRAAL_TRUFFLE" : {
      "subDir" : "graal",
      "dependencies" : [
        "org.graalvm.compiler.truffle",
      ],
      "distDependencies" : [
        "GRAAL_RUNTIME",
        "truffle:TRUFFLE_API",
      ],
    },

    "GRAAL_TRUFFLE_HOTSPOT" : {
      "subDir" : "graal",
      "dependencies" : [
        "org.graalvm.compiler.truffle.hotspot.amd64",
        "org.graalvm.compiler.truffle.hotspot.sparc",
        "org.graalvm.compiler.truffle.hotspot.aarch64",
      ],
      "distDependencies" : [
        "GRAAL_HOTSPOT",
        "GRAAL_TRUFFLE",
        "truffle:TRUFFLE_API",
      ],
    },

    "GRAAL_SERVICEPROVIDER_PROCESSOR" : {
      "subDir" : "graal",
      "dependencies" : ["org.graalvm.compiler.serviceprovider.processor"],
      "distDependencies" : [
        "GRAAL_SERVICEPROVIDER",
      ],
    },

    "GRAAL_NODEINFO_PROCESSOR" : {
      "subDir" : "graal",
      "dependencies" : ["org.graalvm.compiler.nodeinfo.processor"],
      "distDependencies" : [
        "GRAAL_NODEINFO",
      ],
    },

    "GRAAL_REPLACEMENTS_VERIFIER" : {
      "subDir" : "graal",
      "dependencies" : ["org.graalvm.compiler.replacements.verifier"],
      "distDependencies" : [
        "GRAAL_API",
        "GRAAL_SERVICEPROVIDER",
        "GRAAL_SERVICEPROVIDER_PROCESSOR",
      ]
    },

    "GRAAL_COMPILER_MATCH_PROCESSOR" : {
      "subDir" : "graal",
      "dependencies" : ["org.graalvm.compiler.core.match.processor"],
      "distDependencies" : [
        "GRAAL_COMPILER",
        "GRAAL_SERVICEPROVIDER_PROCESSOR",
      ]
    },

    "GRAAL" : {
      # This distribution defines a module.
      "moduleName" : "org.graalvm.compiler.graal_core",
      "subDir" : "graal",
      "overlaps" : [
        "GRAAL_OPTIONS",
        "GRAAL_NODEINFO",
        "GRAAL_API",
        "GRAAL_COMPILER",
        "GRAAL_RUNTIME",
        "GRAAL_HOTSPOT",
        "GRAAL_SERVICEPROVIDER",
        "GRAAL_TRUFFLE",
        "GRAAL_TRUFFLE_HOTSPOT",
      ],
      "dependencies" : [
        "org.graalvm.compiler.options",
        "org.graalvm.compiler.nodeinfo",
        "org.graalvm.compiler.api.replacements",
        "org.graalvm.compiler.api.runtime",
        "org.graalvm.compiler.graph",
        "org.graalvm.compiler.core",
        "org.graalvm.compiler.replacements",
        "org.graalvm.compiler.runtime",
        "org.graalvm.compiler.code",
        "org.graalvm.compiler.printer",
        "org.graalvm.compiler.core.aarch64",
        "org.graalvm.compiler.replacements.aarch64",
        "org.graalvm.compiler.core.amd64",
        "org.graalvm.compiler.replacements.amd64",
        "org.graalvm.compiler.core.sparc",
        "org.graalvm.compiler.replacements.sparc",
        "org.graalvm.compiler.salver",
        "org.graalvm.compiler.hotspot.aarch64",
        "org.graalvm.compiler.hotspot.amd64",
        "org.graalvm.compiler.hotspot.sparc",
        "org.graalvm.compiler.hotspot",
        "org.graalvm.compiler.truffle",
        "org.graalvm.compiler.truffle.hotspot.amd64",
        "org.graalvm.compiler.truffle.hotspot.sparc",
        "org.graalvm.compiler.truffle.hotspot.aarch64",
      ],
      "distDependencies" : [
        "truffle:TRUFFLE_API",
      ],
      "exclude" : [
        "JVMCI_SERVICES",
        "JVMCI_API",
        "JVMCI_HOTSPOT",
      ],
    },
  },
}
