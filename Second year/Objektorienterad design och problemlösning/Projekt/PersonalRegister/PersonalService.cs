using PersonalRegister;
using System;
using System.Text.Json;
using System.Threading.Tasks;

namespace PJU
{
	public class PersonalService
	{
		private readonly JsonPersonalRepository<Ant> _antRepository;
		private readonly JsonPersonalRepository<Bee> _beeRepository;

		public PersonalService(JsonPersonalRepository<Ant> antRepository, JsonPersonalRepository<Bee> beeRepository)
		{
			_antRepository = antRepository;
			_beeRepository = beeRepository;
		}

		public async Task HandleWeeklyOperations(DateTime currentDate, int weekNumber)
		{
			var antFactory = new AntFactory();
			var beeFactory = new BeeFactory();

			// Handle Ants
			int deadAnts = await _antRepository.RemoveDeadPersonalAsync(ant => ((Ant)ant).IsAlive(currentDate));
			Console.WriteLine($"{deadAnts} ants died.");

			int antsToBeBorn = (int)(deadAnts * 1.1); // 10% more ants born than those that died
			if (antsToBeBorn > 0)
			{
				await _antRepository.AddNewPersonalAsync(() => antFactory.Create(currentDate), antsToBeBorn);
				Console.WriteLine($"{antsToBeBorn} new ants were born.");
			}

			// Handle Bees
			int deadBees = await _beeRepository.RemoveDeadPersonalAsync(bee => ((Bee)bee).IsAlive(currentDate));
			Console.WriteLine($"{deadBees} bees died.");

			int beesToBeBorn = (int)(deadBees * 1.2); // 20% more bees born than those that died
			if (beesToBeBorn > 0)
			{
				await _beeRepository.AddNewPersonalAsync(() => beeFactory.Create(currentDate), beesToBeBorn);
				Console.WriteLine($"{beesToBeBorn} new bees were born.");
			}

			// Save state after each operation
			await SaveSimulationStateAsync(currentDate, weekNumber);

			Console.WriteLine($"Total living ants after week {weekNumber}: {_antRepository.GetAll().Count}");
			Console.WriteLine($"Total living bees after week {weekNumber}: {_beeRepository.GetAll().Count}");

			await _antRepository.SaveToFileAsync();
			await _beeRepository.SaveToFileAsync();
		}

		private async Task SaveSimulationStateAsync(DateTime lastSimulatedDate, int weekNumber)
		{
			var simulationState = new SimulationState
			{
				LastSimulatedDate = lastSimulatedDate,
				WeekNumber = weekNumber
			};

			string filePath = "simulation_state.json";
			string json = JsonSerializer.Serialize(simulationState, new JsonSerializerOptions { WriteIndented = true });
			await System.IO.File.WriteAllTextAsync(filePath, json);
		}
	}
}
