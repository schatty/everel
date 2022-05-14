import os
import pickle


class Logger:

    def __init__(self, log_dir, redis_sync_addr=None, save_pickle=False, send_every=100, **kwargs):
        self.data = {"scalars": {}}
        self.log_dir = log_dir

    def add_scalar(self, tag, scalar_value, global_step=None, walltime=None):
        """Add scalar data to summary.

        Args:
            tag (string): Data identifier
            scalar_value (float or string/blobname): Value to save
            global_step (int): Global step value to record
            walltime (float): Optional override default walltime (time.time())
              with seconds after epoch of event
        """
        scalar_value = float(scalar_value)

        if tag not in self.data["scalars"]:
            self.data["scalars"][tag] = {"x": [global_step], "y": [scalar_value]}
            return

        self.data["scalars"][tag]["x"].append(global_step)
        self.data["scalars"][tag]["y"].append(scalar_value)

    def save_data(self):
        fn = os.path.join(self.log_dir, "log.pkl")
        print(f"Saving logging data on: {fn}...")
        with open(fn, "wb") as f:
            pickle.dump(self.data, f)
        print("Data saved.")