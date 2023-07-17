import numpy as np

class Job:
    def __init__(self, start_time, end_time, processing_time):
        self.start_time = start_time
        self.end_time = end_time
        self.processing_time = processing_time
        self.status = 'waiting'  # can be 'waiting', 'processing', 'done'

class Machine:
    def __init__(self, processing_power):
        self.processing_power = processing_power
        self.current_job = None

class Environment:
    def __init__(self, num_jobs, num_machines):
        self.num_jobs = num_jobs
        self.num_machines = num_machines
        self.jobs = [Job(np.random.randint(0, 100), np.random.randint(100, 200), np.random.randint(1, 10)) for _ in range(num_jobs)]
        self.machines = [Machine(np.random.randint(1, 10)) for _ in range(num_machines)]
        self.time = 0

    def reset(self):
        self.jobs = [Job(np.random.randint(0, 100), np.random.randint(100, 200), np.random.randint(1, 10)) for _ in range(self.num_jobs)]
        self.machines = [Machine(np.random.randint(1, 10)) for _ in range(self.num_machines)]
        self.time = 0
        return self.get_state()

    def step(self, action):
        machine, job = action
        if self.machines[machine].current_job is not None or self.jobs[job].status != 'waiting':
            return self.get_state(), -1, False
        self.machines[machine].current_job = self.jobs[job]
        self.jobs[job].status = 'processing'
        for _ in range(self.jobs[job].processing_time):
            self.time += 1
            self.update()
        reward = sum(job.status == 'done' for job in self.jobs)
        done = all(job.status == 'done' for job in self.jobs)
        return self.get_state(), reward, done

    def update(self):
        for machine in self.machines:
            if machine.current_job is not None:
                machine.current_job.processing_time -= machine.processing_power
                if machine.current_job.processing_time <= 0:
                    machine.current_job.status = 'done'
                    machine.current_job = None

    def get_state(self):
        return self.time, [(job.start_time, job.end_time, job.processing_time, job.status) for job in self.jobs]

    def render(self):
        print(f'Time: {self.time}')
        for i, job in enumerate(self.jobs):
            print(f'Job {i}: start_time={job.start_time}, end_time={job.end_time}, processing_time={job.processing_time}, status={job.status}')
        for i, machine in enumerate(self.machines):
            print(f'Machine {i}: processing_power={machine.processing_power}, current_job={self.jobs.index(machine.current_job) if machine.current_job else None}')

    # Other methods as needed
