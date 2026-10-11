class AppConfig {
  static const String appName = 'TideShift';
  static const String version = '1.0.0';

  static const String baseUrl = String.fromEnvironment(
    'BASE_URL',
    defaultValue: 'https://web-production-2ce00.up.railway.app',
  );

  static const String slogan =
      'Build Climate Change Friendly Habits, One Day at a Time';
}
