/*
 * Copyright (c) 2016, 2016, Oracle and/or its affiliates. All rights reserved.
 * DO NOT ALTER OR REMOVE COPYRIGHT NOTICES OR THIS FILE HEADER.
 *
 * This code is free software; you can redistribute it and/or modify it
 * under the terms of the GNU General Public License version 2 only, as
 * published by the Free Software Foundation.  Oracle designates this
 * particular file as subject to the "Classpath" exception as provided
 * by Oracle in the LICENSE file that accompanied this code.
 *
 * This code is distributed in the hope that it will be useful, but WITHOUT
 * ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
 * FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
 * version 2 for more details (a copy is included in the LICENSE file that
 * accompanied this code).
 *
 * You should have received a copy of the GNU General Public License version
 * 2 along with this work; if not, write to the Free Software Foundation,
 * Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA.
 *
 * Please contact Oracle, 500 Oracle Parkway, Redwood Shores, CA 94065 USA
 * or visit www.oracle.com if you need additional information or have any
 * questions.
 */
package com.oracle.graal.truffle.nodes;

import java.lang.invoke.MethodHandle;
import java.lang.invoke.MethodHandles;
import java.lang.invoke.MethodType;
import java.lang.reflect.Method;
import java.lang.reflect.Modifier;

import com.oracle.truffle.api.CompilerDirectives.TruffleBoundary;
import com.oracle.truffle.api.nodes.JavaMethodCallNode;

/**
 * This is runtime specific API. Do not use in a guest language.
 */
public final class MethodHandleJavaMethodCallNode extends JavaMethodCallNode {
    protected final MethodHandle methodHandle;

    private MethodHandleJavaMethodCallNode(MethodHandle methodHandle) {
        assert methodHandle.type().equals(MethodType.methodType(Object.class, Object.class, Object[].class));
        this.methodHandle = methodHandle;
    }

    @TruffleBoundary(throwsControlFlowException = true)
    @Override
    public Object invoke(Object obj, Object[] arguments) throws Throwable {
        return methodHandle.invokeExact(obj, arguments);
    }

    public static JavaMethodCallNode create(Method reflectionMethod) {
        final MethodHandle methodHandle;
        try {
            methodHandle = MethodHandles.publicLookup().unreflect(reflectionMethod);
        } catch (IllegalAccessException e) {
            throw new RuntimeException(e);
        }
        return new MethodHandleJavaMethodCallNode(adaptSignature(methodHandle, Modifier.isStatic(reflectionMethod.getModifiers()), reflectionMethod.getParameterCount()));
    }

    private static MethodHandle adaptSignature(MethodHandle originalHandle, boolean isStatic, int parameterCount) {
        MethodHandle adaptedHandle = originalHandle;
        adaptedHandle = adaptedHandle.asType(adaptedHandle.type().changeReturnType(Object.class));
        if (isStatic) {
            adaptedHandle = MethodHandles.dropArguments(adaptedHandle, 0, Object.class);
        } else {
            adaptedHandle = adaptedHandle.asType(adaptedHandle.type().changeParameterType(0, Object.class));
        }
        adaptedHandle = adaptedHandle.asSpreader(Object[].class, parameterCount);
        return adaptedHandle;
    }
}
