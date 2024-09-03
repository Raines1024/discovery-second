import pm4py
import sys


if __name__ == "__main__":

    # 加载 .xes 文件
    BPIC13_i = pm4py.read_xes('BPIC13_i.xes')
    BPIC13_cp = pm4py.read_xes('BPIC13_cp.xes')
    BPIC15_1f = pm4py.read_xes("BPIC15_1f.xes")
    BPIC15_2f = pm4py.read_xes("BPIC15_2f.xes")
    BPIC15_4f = pm4py.read_xes("BPIC15_4f.xes")
    BPIC15_5f = pm4py.read_xes("BPIC15_5f.xes")


    if len(sys.argv) > 1:
        # 获取第一个命令行参数
        param = sys.argv[1]
        print(f"第一个命令行参数是: {param}")
        if param == "powl":
            # 从事件日志中发现 POWL 模型
            powl_model = pm4py.discover_powl(BPIC13_i, activity_key='concept:name')
            powl_model = pm4py.discover_powl(BPIC13_cp, activity_key='concept:name')
            powl_model = pm4py.discover_powl(BPIC15_1f, activity_key='concept:name')
            powl_model = pm4py.discover_powl(BPIC15_2f, activity_key='concept:name')
            powl_model = pm4py.discover_powl(BPIC15_4f, activity_key='concept:name')
            powl_model = pm4py.discover_powl(BPIC15_5f, activity_key='concept:name')
        elif param == "declare":
            # 从事件日志中发现 DECLARE 模型
            declare_model = pm4py.discover_declare(BPIC13_i)
            declare_model = pm4py.discover_declare(BPIC13_cp)
            declare_model = pm4py.discover_declare(BPIC15_1f)
            declare_model = pm4py.discover_declare(BPIC15_2f)
            declare_model = pm4py.discover_declare(BPIC15_4f)
            declare_model = pm4py.discover_declare(BPIC15_5f)

        elif param == "performance_dfg":
            # 从事件日志中发现性能直接跟踪图
            performance_dfg, start_activities, end_activities = pm4py.discover_performance_dfg(BPIC13_i, case_id_key='case:concept:name', activity_key='concept:name', timestamp_key='time:timestamp')
            performance_dfg, start_activities, end_activities = pm4py.discover_performance_dfg(BPIC13_cp, case_id_key='case:concept:name', activity_key='concept:name', timestamp_key='time:timestamp')
            performance_dfg, start_activities, end_activities = pm4py.discover_performance_dfg(BPIC15_1f, case_id_key='case:concept:name', activity_key='concept:name', timestamp_key='time:timestamp')
            performance_dfg, start_activities, end_activities = pm4py.discover_performance_dfg(BPIC15_2f, case_id_key='case:concept:name', activity_key='concept:name', timestamp_key='time:timestamp')
            performance_dfg, start_activities, end_activities = pm4py.discover_performance_dfg(BPIC15_4f, case_id_key='case:concept:name', activity_key='concept:name', timestamp_key='time:timestamp')
            performance_dfg, start_activities, end_activities = pm4py.discover_performance_dfg(BPIC15_5f, case_id_key='case:concept:name', activity_key='concept:name', timestamp_key='time:timestamp')

        elif param == "temporal_profile":
            # 从日志对象中发现时间剖面
            temporal_profile = pm4py.discover_temporal_profile(BPIC13_i, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
            temporal_profile = pm4py.discover_temporal_profile(BPIC13_cp, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
            temporal_profile = pm4py.discover_temporal_profile(BPIC15_1f, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
            temporal_profile = pm4py.discover_temporal_profile(BPIC15_2f, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
            temporal_profile = pm4py.discover_temporal_profile(BPIC15_4f, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
            temporal_profile = pm4py.discover_temporal_profile(BPIC15_5f, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')

        elif param == "process_tree_inductive":
            # 使用归纳矿工算法发现进程树
            process_tree = pm4py.discover_process_tree_inductive(BPIC13_i, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
            process_tree = pm4py.discover_process_tree_inductive(BPIC13_cp, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
            process_tree = pm4py.discover_process_tree_inductive(BPIC15_1f, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
            process_tree = pm4py.discover_process_tree_inductive(BPIC15_2f, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
            process_tree = pm4py.discover_process_tree_inductive(BPIC15_4f, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
            process_tree = pm4py.discover_process_tree_inductive(BPIC15_5f, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')

    else:
        print("没有提供任何命令行参数")


