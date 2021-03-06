/*
 * Copyright (c) 2009, 2015, Oracle and/or its affiliates. All rights reserved.
 * DO NOT ALTER OR REMOVE COPYRIGHT NOTICES OR THIS FILE HEADER.
 *
 * This code is free software; you can redistribute it and/or modify it
 * under the terms of the GNU General Public License version 2 only, as
 * published by the Free Software Foundation.
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
package com.oracle.graal.nodes.java;

import jdk.vm.ci.code.BailoutException;

import com.oracle.graal.compiler.common.type.StampFactory;
import com.oracle.graal.graph.NodeClass;
import com.oracle.graal.nodeinfo.InputType;
import com.oracle.graal.nodeinfo.NodeInfo;
import com.oracle.graal.nodes.DeoptimizingNode;
import com.oracle.graal.nodes.FrameState;
import com.oracle.graal.nodes.ValueNode;
import com.oracle.graal.nodes.memory.AbstractMemoryCheckpoint;
import com.oracle.graal.nodes.memory.MemoryCheckpoint;

/**
 * The {@code AccessMonitorNode} is the base class of both monitor acquisition and release.
 * <p>
 * The Java bytecode specification allows non-balanced locking. Graal does not handle such cases and
 * throws a {@link BailoutException} instead during graph building.
 */
@NodeInfo(allowedUsageTypes = {InputType.Memory})
public abstract class AccessMonitorNode extends AbstractMemoryCheckpoint implements MemoryCheckpoint, DeoptimizingNode.DeoptBefore, DeoptimizingNode.DeoptAfter {

    public static final NodeClass<AccessMonitorNode> TYPE = NodeClass.create(AccessMonitorNode.class);
    @OptionalInput(InputType.State) FrameState stateBefore;
    @Input ValueNode object;
    @Input(InputType.Association) MonitorIdNode monitorId;

    @Override
    public boolean canDeoptimize() {
        return true;
    }

    public FrameState stateBefore() {
        return stateBefore;
    }

    @Override
    public void setStateBefore(FrameState f) {
        updateUsages(stateBefore, f);
        stateBefore = f;
    }

    public ValueNode object() {
        return object;
    }

    public MonitorIdNode getMonitorId() {
        return monitorId;
    }

    /**
     * Creates a new AccessMonitor instruction.
     *
     * @param object the instruction producing the object
     */
    protected AccessMonitorNode(NodeClass<? extends AccessMonitorNode> c, ValueNode object, MonitorIdNode monitorId) {
        super(c, StampFactory.forVoid());
        this.object = object;
        this.monitorId = monitorId;
    }
}
